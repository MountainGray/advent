const std = @import("std");

pub fn build(b: *std.Build) void {

    // Set build commands for each day
    var day: u32 = 1;
    while (day <= 25) : (day += 1) {
        const dayString = b.fmt("day{:0>2}", .{day});
        const zigFile = b.fmt("src/{s}.zig", .{dayString});
        const exe = b.addExecutable(.{
            .name = dayString,
            .root_source_file = .{ .path = zigFile }
        });

        b.installArtifact(exe);

        const run_exe = b.addRunArtifact(exe);
        const run_desc = b.fmt("Run {s}", .{dayString});
        const run_step = b.step(dayString, run_desc);
        run_step.dependOn(&run_exe.step);
    }
}
