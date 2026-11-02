import datetime
import json
import pathlib
import time
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
URL = "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD6/deg11_diam6_n186033_networkx.adjlist.gz"
start = time.monotonic()
dest = HERE / "source186033.adjlist.gz"
partial = HERE / "source186033.adjlist.gz.partial"
status = {"status": "DOWNLOADING", "url": URL, "file": str(dest),
          "bytes": 0, "started_UTC": datetime.datetime.now(datetime.timezone.utc).isoformat()}
(HERE / "DOWNLOAD_HANDLE.json").write_text(json.dumps(status, indent=2) + "\n")
try:
    req = urllib.request.Request(URL, headers={"User-Agent": "ar4math source research"})
    with urllib.request.urlopen(req, timeout=90) as response, partial.open("wb") as out:
        status["http_status"] = response.status
        status["content_length"] = response.headers.get("Content-Length")
        while chunk := response.read(262144):
            out.write(chunk)
            status["bytes"] += len(chunk)
            status["elapsed_wall_seconds"] = time.monotonic() - start
            (HERE / "DOWNLOAD_HANDLE.json").write_text(json.dumps(status, indent=2) + "\n")
    partial.replace(dest)
    status["status"] = "COMPLETE"
except Exception as exc:
    status["status"] = "SOURCE_NOT_YET_BOUND"
    status["error"] = str(exc)
status["elapsed_wall_seconds"] = time.monotonic() - start
(HERE / "DOWNLOAD_HANDLE.json").write_text(json.dumps(status, indent=2) + "\n")
print(json.dumps(status, indent=2))
