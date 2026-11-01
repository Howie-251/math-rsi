"""MathRSI integration gaps beyond the vendored ARIS protocol tests.

These run the bundled servers with fake CLI processes only. No model API calls.
The original per-server Clients remain test fixtures, not a new runtime client.
"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

import test_antigravity_exec_bridge as agy
import test_codex_exec_bridge as codex
import test_grok_exec_bridge as grok


def assert_reaped(test, pid):
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return
        time.sleep(0.02)
    test.fail(f"fake CLI pid {pid} remains after bridge cleanup")


class GeminiFourTests(unittest.TestCase):
    def setUp(self):
        agy.BridgeTests.setUp(self)

    def tearDown(self):
        agy.BridgeTests.tearDown(self)

    def test_explicit_gemini_four_request_and_restart_reply(self):
        first = self.client.call(1, "antigravity", {
            "prompt": "first", "model": "gemini-4-argon-high", "effort": "high",
            "cwd": str(self.root),
        })["result"]["structuredContent"]
        self.assertEqual(first["requestedModel"], "gemini-4-argon-high")
        self.assertEqual(first["model"], "gemini-4-argon-high")
        self.client.close()
        self.client = agy.Client(self.env, self.root)
        reply = self.client.call(2, "antigravity-reply", {
            "threadId": first["threadId"], "prompt": "second",
        })["result"]["structuredContent"]
        self.assertEqual(reply["threadId"], first["threadId"])
        self.assertEqual(reply["requestedModel"], "gemini-4-argon-high")

    @unittest.skipUnless(os.name == "posix", "PID lifecycle check uses POSIX kill(0)")
    def test_timeout_reaps_actual_cli_child(self):
        self.client.close()
        fake = self.root / "antigravity"
        fake.write_text(agy.FAKE.replace("'cwd':os.getcwd()", "'cwd':os.getcwd(),'pid':os.getpid()"))
        self.env["AGY_EXEC_TIMEOUT_SEC"] = "2"
        self.client = agy.Client(self.env, self.root)
        result = self.client.call(1, "antigravity", {"prompt": "SLOW"})["result"]
        self.assertTrue(result["isError"])
        self.assertIn("timed out", result["content"][0]["text"])
        pid = json.loads(self.log.read_text().splitlines()[0])["pid"]
        assert_reaped(self, pid)


class GrokCleanupTests(unittest.TestCase):
    def setUp(self):
        grok.BridgeTests.setUp(self)

    def tearDown(self):
        grok.BridgeTests.tearDown(self)

    @unittest.skipUnless(os.name == "posix", "PID lifecycle check uses POSIX kill(0)")
    def test_host_disconnect_reaps_actual_cli_child(self):
        fake = self.root / "grok"
        fake.write_text(grok.FAKE.replace("'cwd':os.getcwd()", "'cwd':os.getcwd(),'pid':os.getpid()"))
        self.client.send({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {
            "name": "grok", "arguments": {"prompt": "SLOW"},
        }})
        deadline = time.monotonic() + 3
        while not self.log.exists() and time.monotonic() < deadline:
            time.sleep(0.02)
        pid = json.loads(self.log.read_text().splitlines()[0])["pid"]
        self.client.stdin.close()
        self.assertTrue(self.client.recv(1)["result"]["isError"])
        self.client.proc.wait(timeout=3)
        assert_reaped(self, pid)


class CodexRestartTests(unittest.TestCase):
    def setUp(self):
        codex.BridgeTests.setUp(self)

    def tearDown(self):
        codex.BridgeTests.tearDown(self)

    def test_resume_after_bridge_restart_uses_persisted_settings(self):
        first = self.bridge.call(2, "codex", {
            "prompt": "first", "model": "gpt-6-astra", "sandbox": "read-only",
            "cwd": str(self.tmp), "config": {"model_reasoning_effort": "ultra"},
        })["result"]["structuredContent"]
        self.bridge.close()
        self.bridge = codex.BridgeProcess(self.env, cwd=str(self.tmp))
        second = self.bridge.call(3, "codex-reply", {
            "threadId": first["threadId"], "prompt": "second",
        })["result"]["structuredContent"]
        self.assertEqual(second["threadId"], first["threadId"])
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        self.assertIn('model_reasoning_effort="ultra"', calls[1]["argv"])
        self.assertIn('sandbox_mode="read-only"', calls[1]["argv"])
        self.assertEqual(calls[1]["argv"][calls[1]["argv"].index("-m") + 1], "gpt-6-astra")


FAKE_CLAUDE = r'''#!/usr/bin/env python3
import json, os, sys, time
a=sys.argv[1:]
def arg(k): return a[a.index(k)+1]
prompt=arg('-p')
tid=arg('--resume') if '--resume' in a else 'fake-claude-session'
with open(os.environ['FAKE_CLAUDE_LOG'],'a') as f:
 f.write(json.dumps({'argv':a,'cwd':os.getcwd(),'pid':os.getpid()})+'\n')
if prompt=='SLOW': time.sleep(5)
result={'type':'result','subtype':'error' if prompt=='FAIL' else 'success',
 'is_error':prompt=='FAIL','result':'' if prompt=='EMPTY' else 'echo:'+prompt,
 'session_id':tid,'stop_reason':'max_tokens' if prompt=='TRUNC' else 'end_turn',
 'modelUsage':{'configured-provider-model':{}}}
print(json.dumps(result))
'''


class ClaudeProcessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="mathrsi-claude-")
        self.root = Path(self.tmp.name).resolve()
        fake = self.root / "claude"
        fake.write_text(FAKE_CLAUDE)
        fake.chmod(0o755)
        self.log = self.root / "calls.jsonl"
        self.env = dict(os.environ, CLAUDE_BIN=str(fake),
            CLAUDE_REVIEW_STATE_DIR=str(self.root / "state"),
            CLAUDE_REVIEW_DEBUG_LOG=str(self.root / "debug.log"),
            CLAUDE_REVIEW_TIMEOUT_SEC="1", FAKE_CLAUDE_LOG=str(self.log))
        self.server = Path(__file__).resolve().parents[1] / "claude-review/server.py"
        self.start()

    def start(self):
        self.proc = subprocess.Popen([sys.executable, str(self.server)], cwd=self.root,
            env=self.env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True)

    def stop(self):
        self.proc.stdin.close()
        self.proc.wait(timeout=4)
        self.proc.stdout.close()
        self.proc.stderr.close()

    def tearDown(self):
        self.stop()
        self.tmp.cleanup()

    def rpc(self, method, params=None):
        self.proc.stdin.write(json.dumps({"jsonrpc":"2.0","id":1,
            "method":method,"params":params or {}}) + "\n")
        self.proc.stdin.flush()
        return json.loads(self.proc.stdout.readline())

    def call(self, name, args):
        result = self.rpc("tools/call", {"name":name,"arguments":args})["result"]
        return result, json.loads(result["content"][0]["text"])

    def test_stdio_schema_and_explicit_artifact_tools_on_reply(self):
        init = self.rpc("initialize", {"protocolVersion":"2025-06-18"})
        self.assertEqual(init["result"]["serverInfo"]["name"], "claude-review")
        listing = self.rpc("tools/list")["result"]["tools"]
        self.assertEqual({x["name"] for x in listing}, {
            "review","review_reply","review_start","review_reply_start","review_status"})
        args = {"prompt":"first","cwd":str(self.root),"tools":"Read,Grep,Glob","model":"requested-alias"}
        _, first = self.call("review", args)
        self.assertEqual(first["requestedModel"], "requested-alias")
        self.assertEqual(first["model"], "configured-provider-model")
        self.stop()
        self.start()
        _, reply = self.call("review_reply", dict(args, prompt="second", threadId=first["threadId"]))
        self.assertEqual(reply["threadId"], first["threadId"])
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        self.assertIn("--resume", calls[1]["argv"])
        self.assertEqual(calls[1]["argv"][calls[1]["argv"].index("--tools")+1], "Read,Grep,Glob")
        self.assertEqual(calls[1]["cwd"], str(self.root))

    def test_async_status_survives_bridge_restart(self):
        _, started = self.call("review_start", {"prompt":"async","cwd":str(self.root),"tools":"Read,Grep,Glob"})
        self.stop()
        self.start()
        _, status = self.call("review_status", {"jobId":started["jobId"],"waitSeconds":3})
        self.assertTrue(status["done"])
        self.assertEqual(status["status"], "completed")
        self.assertEqual(status["response"], "echo:async")

    def test_fail_empty_truncated_timeout_and_timeout_child_cleanup(self):
        for prompt in ["FAIL", "EMPTY", "TRUNC", "SLOW"]:
            with self.subTest(prompt=prompt):
                result, payload = self.call("review", {"prompt":prompt,"cwd":str(self.root)})
                self.assertTrue(result["isError"])
                self.assertTrue(payload["error"])
        if os.name == "posix":
            pid = json.loads(self.log.read_text().splitlines()[-1])["pid"]
            assert_reaped(self, pid)


if __name__ == "__main__":
    unittest.main()
