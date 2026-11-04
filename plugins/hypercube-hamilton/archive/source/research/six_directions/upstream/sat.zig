const std = @import("std");
const utils = @import("utils.zig");
const clap = @import("clap");

const c = @cImport({
    @cInclude("ccadical.h");
});

const Literal = c_int;
const Literals = std.ArrayList(Literal);

/// Wrapper object around the C-object for CaDiCaL
const Solver = struct {
    solver: ?*c.struct_CCaDiCaL,

    const Self = @This();

    const Data = struct { max_id: Literal };

    pub fn init() Self {
        return .{
            .solver = c.ccadical_init(),
        };
    }

    pub fn deinit(self: *Self) void {
        c.ccadical_release(self.solver);
    }

    pub fn add(self: *Self, lit: Literal) void {
        c.ccadical_add(self.solver, lit);
    }

    pub fn assume(self: *Self, lit: Literal) void {
        c.ccadical_assume(self.solver, lit);
    }

    pub const Result = enum(c_int) { satisfiable = 10, unsatisfiable = 20, unknown = 0 };

    pub fn solve(self: *Self) Result {
        return @enumFromInt(c.ccadical_solve(self.solver));
    }

    pub fn val(self: *Self, lit: Literal) Literal {
        return c.ccadical_val(self.solver, lit);
    }

    pub fn clauseBuilder(self: *Self) ClauseBuilder {
        return ClauseBuilder.init(self);
    }
};

/// Utility for adding clauses to the solver
const ClauseBuilder = struct {
    solver: *Solver,
    max_variable: Literal,

    const Self = @This();

    pub fn init(solver: *Solver) Self {
        return .{
            .solver = solver,
            .max_variable = 1,
        };
    }

    pub fn add(self: *Self, lit: Literal) !void {
        self.solver.add(lit);
    }

    pub fn addClause(self: *Self, clause: anytype) !void {
        inline for (clause) |lit| {
            try self.add(lit);
        }

        try self.add(0);
    }
};

/// Object, that maintains the latest variable ID added to a solver, needs to be deinitialized
const ConsecutiveIDPool = struct {
    current_id: *Literal,
    allocator: std.mem.Allocator,

    const Self = @This();

    pub fn init(allocator: std.mem.Allocator, from: Literal) !Self {
        const data = try allocator.create(Literal);
        data.* = from;
        return .{ .allocator = allocator, .current_id = data };
    }

    pub fn deinit(self: *Self) void {
        self.allocator.destroy(self.current_id);
    }

    pub fn next(self: *Self) Literal {
        const to_return = self.current_id.*;
        self.current_id.* = self.current_id.* + 1;
        return to_return;
    }
};

/// Utility containing and IDPool and ClauseBuilder for the Solver
const SolverUtils = struct {
    clause_builder: ClauseBuilder,
    id_pool: ConsecutiveIDPool,
    allocator: std.mem.Allocator,

    const Self = @This();

    pub fn init(solver: *Solver, allocator: std.mem.Allocator) !Self {
        return .{
            .clause_builder = solver.clauseBuilder(),
            .id_pool = try ConsecutiveIDPool.init(allocator, 1),
            .allocator = allocator,
        };
    }

    pub fn deinit(self: *Self) void {
        self.id_pool.deinit();
    }
};

/// Wrapper type around a custom type getting you custom ids for custom objects. For example let
/// Vertex by type representing a vertex of your graph and let's say you would need a variable
/// for each such vertex. This type gives you thet possibility.
pub fn IDPool(comptime T: type) type {
    return struct {
        id_pool: ConsecutiveIDPool,
        memory: Memory,

        const Self = @This();

        const Memory = std.AutoHashMap(T, Literal);

        pub fn init(allocator: std.mem.Allocator, id_pool: ConsecutiveIDPool) Self {
            return .{
                .id_pool = id_pool,
                .memory = Memory.init(allocator),
            };
        }

        pub fn deinit(self: *Self) void {
            self.memory.deinit();
        }

        /// Get variable corresponding to the object
        pub fn get(self: *Self, key: T) !Literal {
            const r = try self.memory.getOrPut(key);

            if (!r.found_existing) {
                r.value_ptr.* = self.id_pool.next();
            }

            return r.value_ptr.*;
        }
    };
}

pub fn BaseCasesUtils(comptime D: comptime_int) type {
    const H = utils.HyperCube(D);

    return struct {
        const ToAvoid = [H.vertex_count]bool;
        const ToAvoidResult = std.ArrayList(ToAvoid);
        const ToAvoidSeenSet = std.AutoArrayHashMap(ToAvoid, void);

        /// Utility for debugging of the ToAvoid set
        const ToAvoidFormatted = struct {
            to_avoid: ToAvoid,

            const Self = @This();

            pub fn format(
                self: Self,
                comptime _: []const u8,
                _: std.fmt.FormatOptions,
                writer: anytype,
            ) !void {
                for (self.to_avoid) |v| {
                    if (v) {
                        try writer.print("X", .{});
                    } else {
                        try writer.print("-", .{});
                    }
                }
            }
        };

        /// Given automorphism transform the holes to avoid via that automorphism
        pub fn transformToAvoid(automorphism: H.Automorphism, to_avoid: ToAvoid) ToAvoid {
            var result: ToAvoid = undefined;

            for (0.., automorphism.vertices) |ix, vertex| {
                result[ix] = to_avoid[vertex];
            }

            return result;
        }

        /// Generate all of the holes to avoid up to an isomorphism
        pub fn generateToAvoid(allocator: std.mem.Allocator) !ToAvoidResult {
            // Start with no vertex to avoid
            var to_avoid_empty: ToAvoid = undefined;
            @memset(&to_avoid_empty, false);

            var result = ToAvoidResult.init(allocator);
            errdefer result.deinit();
            try result.append(to_avoid_empty);

            // Get all of the automorphisms
            const automorphisms = H.generateAllAutomorphisms();

            var current_level: usize = 0;
            var current_level_base = ToAvoidResult.init(allocator);
            defer current_level_base.deinit();
            try current_level_base.append(to_avoid_empty);
            var next_level_base = ToAvoidResult.init(allocator);
            defer next_level_base.deinit();
            var next_level_already_seen = ToAvoidSeenSet.init(allocator);
            defer next_level_already_seen.deinit();

            // For each level represented by number of holes, take all of the configurations from
            // previous level and try to add one new hole to them. Add all automorphisms to already
            // seen set, to prevent isomorphisms of being added.
            while (true) {
                current_level += 1;

                next_level_base.clearRetainingCapacity();
                next_level_already_seen.clearRetainingCapacity();

                for (current_level_base.items) |base_to_avoid| {
                    // Try each of possible vertices to be avoided
                    vertex: for (0..H.vertex_count) |vertex_num| {
                        const vertex: H.Vertex = @intCast(vertex_num);

                        // If already avoided we are done
                        if (base_to_avoid[vertex]) continue;

                        // Check whether we can avoid that vertex (we can't avoid two neighbors)
                        for (H.dims) |dim| {
                            if (base_to_avoid[H.vertexNeighbour(vertex, dim)]) continue :vertex;
                        }

                        // Create a new configuration with the new vertex to be avoided
                        var new_to_avoid = base_to_avoid;
                        new_to_avoid[vertex] = true;

                        // If already seen continue
                        if (next_level_already_seen.contains(new_to_avoid)) continue;

                        try next_level_base.append(new_to_avoid);

                        // If even number of vertices avoided add it to result
                        if (current_level % 2 == 0) {
                            try result.append(new_to_avoid);
                        }

                        // Add all of the isomorphisms
                        for (automorphisms) |automorphism| {
                            const transformed_to_avoid = transformToAvoid(
                                automorphism,
                                new_to_avoid,
                            );

                            try next_level_already_seen.put(transformed_to_avoid, {});
                        }
                    }
                }

                // Switch the current and next level sets
                const tmp = current_level_base;
                current_level_base = next_level_base;
                next_level_base = tmp;

                if (next_level_base.items.len == 0) break;
            }

            return result;
        }
    };
}

/// Since we are running the generator in multiple threads, ensure that we are writing to stdout
/// only in one thread at once
var stdout_mutex: std.Thread.Mutex = .{};

/// Generate all maximal matchings avoiding given set of vertices and possible avoiding even the
/// zero vertex
pub fn generateMaximalMatchings(
    comptime D: comptime_int,
    allocator: std.mem.Allocator,
    to_avoid: BaseCasesUtils(D).ToAvoid,
    omit_zero: bool,
) !void {
    var solver = Solver.init();
    defer solver.deinit();
    var u = try SolverUtils.init(
        &solver,
        allocator,
    );
    defer u.deinit();

    const H = utils.HyperCube(D);

    // The isomorphisms that we will throw out
    const automorphisms = H.generateAllAutomorphisms();

    const EdgePool = IDPool(H.Edge);
    const VertexPool = IDPool(H.Vertex);
    const MatchingSeenSet = std.AutoHashMap(H.Matching, void);

    // We keep of matchings that we have already seen up to isomorphism
    var matching_already_seen = MatchingSeenSet.init(allocator);
    defer matching_already_seen.deinit();

    // Variables pool for edge
    var edge_id_pool = EdgePool.init(allocator, u.id_pool);
    // Simplified number representing an edge to variable
    var edge_to_var: [H.edge_count]Literal = undefined;
    // Simplified number to edge
    var edges: [H.edge_count]H.Edge = undefined;

    for (0..H.edge_count) |i| {
        const e = H.Edge.fromInt(@intCast(i));

        edge_to_var[i] = try edge_id_pool.get(e);
        edges[i] = e;
    }

    // Variables pool for vertices
    var vertex_id_pool = VertexPool.init(allocator, u.id_pool);
    // Simplified number to vertex
    var vertex_to_var: [H.vertex_count]Literal = undefined;

    for (0..H.vertex_count) |i| {
        vertex_to_var[i] = try vertex_id_pool.get(@intCast(i));

        if (to_avoid[i]) {
            try u.clause_builder.addClause(.{-vertex_to_var[i]});
        } else {
            try u.clause_builder.addClause(.{vertex_to_var[i]});
        }
    }

    // No two incident edges at once
    for (0..H.edge_count) |i| {
        for ((i + 1)..H.edge_count) |j| {
            if (edges[i].incident(edges[j])) {
                try u.clause_builder.addClause(.{ -edge_to_var[i], -edge_to_var[j] });
            }
        }
    }

    // Edge uv in matching implies that vertices u and v are covered
    for (0..H.edge_count) |i| {
        try u.clause_builder.addClause(.{ -edge_to_var[i], vertex_to_var[edges[i].a] });
        try u.clause_builder.addClause(.{ -edge_to_var[i], vertex_to_var[edges[i].b] });
    }

    // That vertex v is covered implies, that one of the incident edges must be in the matching
    for (0..H.vertex_count) |i| {
        const v: H.Vertex = @intCast(i);

        for (H.dims) |d| {
            const e = H.Edge.make(v, H.vertexNeighbour(v, d));

            try u.clause_builder.add(edge_to_var[e.asInt()]);
        }

        try u.clause_builder.add(-vertex_to_var[i]);
        try u.clause_builder.add(0);
    }

    // One of two neighbors must be covered for the matching to be maximal (since otherwise we
    // could add an edge between them)
    for (0..H.vertex_count) |i| {
        for ((i + 1)..H.vertex_count) |j| {
            const v1: H.Vertex = @intCast(i);
            const v2: H.Vertex = @intCast(j);

            if (!H.areNeighbours(v1, v2)) {
                continue;
            }

            try u.clause_builder.addClause(.{ vertex_to_var[i], vertex_to_var[j] });
        }
    }

    // If zero is avoided, avoid that vertex and force all vertices around
    if (omit_zero) {
        try u.clause_builder.addClause(.{-vertex_to_var[0]});

        for (H.dims) |dim| {
            const n = H.vertexNeighbour(0, dim);

            try u.clause_builder.addClause(.{vertex_to_var[n]});
        }
    }

    var w = std.io.getStdOut().writer();

    // Generate matchings until no other matching exist
    while (true) {
        const result = solver.solve();

        // We can't generate another matching
        if (result == .unsatisfiable) {
            break;
        }

        // Get the generated matching from the solver
        var present_edges: [H.edge_count]bool = undefined;
        var matching = H.emptyMatching();
        var edges_count: usize = 0;

        for (0..H.edge_count) |i| {
            present_edges[i] = solver.val(edge_to_var[i]) > 0;

            if (present_edges[i]) {
                matching[edges[i].a] = .{ .vertex = edges[i].b };
                matching[edges[i].b] = .{ .vertex = edges[i].a };
                edges_count += 1;
            }
        }

        // Write the matching to output
        {
            stdout_mutex.lock();
            defer stdout_mutex.unlock();
            try w.print("{} ", .{edges_count});
            for (0.., present_edges) |i, v| {
                if (!v) continue;

                try w.print("{}", .{i});
                edges_count -= 1;
                if (edges_count != 0) try w.print(" ", .{});
            }

            try w.print("\n", .{});
        }

        // Add all automorphisms to the seen set
        for (automorphisms) |a| {
            const transformed_matching = a.transformMatching(matching);

            // If already seen this variation of the matching skip
            if (matching_already_seen.contains(transformed_matching)) {
                continue;
            }

            // Otherwise put it into the seen set
            try matching_already_seen.put(transformed_matching, {});

            // And also say to solver that we do not want to generate that matching
            const transformed_matching_edges = H.matchingToMatchingEdges(transformed_matching);
            var transformed_seen_edges: [H.edge_count]bool = undefined;
            @memset(&transformed_seen_edges, false);

            for (transformed_matching_edges.constSlice()) |edge| {
                transformed_seen_edges[edge.asInt()] = true;
            }

            for (transformed_seen_edges, 0..) |v, i| {
                if (!v) {
                    try u.clause_builder.add(edge_to_var[i]);
                }
            }

            try u.clause_builder.add(0);
        }
    }
}

// Utility to process data in parallel in multiple threads
fn Worker(comptime T: type) type {
    return struct {
        const Queue = std.DoublyLinkedList(T);
        const Context = struct {
            allocator: std.mem.Allocator,
            mutex: *std.Thread.Mutex,
            queue: *Queue,
        };

        pub fn run(context: Context, run_context: anytype) !void {
            while (true) {
                const data: ?T = data: {
                    context.mutex.lock();
                    defer context.mutex.unlock();

                    const data = context.queue.pop();

                    if (data) |inner_data| {
                        const tmp = inner_data.data;

                        context.allocator.destroy(inner_data);

                        break :data tmp;
                    } else {
                        break :data null;
                    }
                };

                if (data) |inner_data| {
                    try run_context.run(inner_data);
                } else {
                    break;
                }
            }
        }

        pub fn processArrayList(allocator: std.mem.Allocator, run_context: anytype, data: std.ArrayList(T), num_threads: usize) !void {
            var queue: Queue = .{};

            for (data.items) |item| {
                const node = try allocator.create(Queue.Node);
                node.* = .{ .data = item };
                queue.append(node);
            }

            var mutex: std.Thread.Mutex = .{};

            const context: Context = .{
                .allocator = allocator,
                .mutex = &mutex,
                .queue = &queue,
            };

            const Threads = std.ArrayList(std.Thread);
            var threads = try Threads.initCapacity(allocator, num_threads);

            for (0..num_threads) |_| {
                try threads.append(try std.Thread.spawn(.{}, run, .{ context, run_context }));
            }

            for (threads.items) |thread| {
                thread.join();
            }
        }
    };
}

pub fn run_main(comptime D: comptime_int, allocator: std.mem.Allocator, threads: usize, omit_zero: bool) !void {
    const B = BaseCasesUtils(D);

    const to_process = try B.generateToAvoid(allocator);
    defer to_process.deinit();

    const Run = struct {
        allocator: std.mem.Allocator,
        omit_zero: bool,

        const Self = @This();

        pub fn run(self: Self, item: B.ToAvoid) !void {
            try generateMaximalMatchings(D, self.allocator, item, self.omit_zero);
        }
    };

    try Worker(B.ToAvoid).processArrayList(
        allocator,
        Run{ .allocator = allocator, .omit_zero = omit_zero },
        to_process,
        threads,
    );
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const params = comptime clap.parseParamsComptime(
        \\-h, --help                Display this help and exit.
        \\-d, --dimension <usize>   Optionally specified dimension, default is 5, accept values between 2 and 5
        \\-t, --threads <usize>     Number of threads spawned to parallelize the workload
        \\-o, --omit                Should be zero vertex omitted
        \\
    );

    var diag = clap.Diagnostic{};
    var res = clap.parse(clap.Help, &params, clap.parsers.default, .{
        .diagnostic = &diag,
        .allocator = allocator,
    }) catch |err| {
        // Report useful error and exit.
        diag.report(std.io.getStdErr().writer(), err) catch {};
        return err;
    };
    defer res.deinit();

    const dimension = res.args.dimension orelse 5;
    const threads = res.args.threads orelse 10;
    const omit_zero = res.args.omit > 0;

    // Not the cleanest way, to do this, but needed for comptime magic
    if (dimension == 2) {
        try run_main(2, allocator, threads, omit_zero);
    } else if (dimension == 3) {
        try run_main(3, allocator, threads, omit_zero);
    } else if (dimension == 4) {
        try run_main(4, allocator, threads, omit_zero);
    } else if (dimension == 5) {
        try run_main(5, allocator, threads, omit_zero);
    } else {
        std.debug.print("Invalid dimension {}", .{dimension});
    }
}
