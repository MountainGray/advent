const std = @import("std");
const Allocator = std.mem.Allocator;
const List = std.ArrayList;
const Map = std.AutoHashMap;
const StrMap = std.StringHashMap;
const BitSet = std.DynamicBitSet;
var gpa_impl = std.heap.GeneralPurposeAllocator(.{}){};
pub const gpa = gpa_impl.allocator();


const data = @embedFile("data/2018/day01.txt");


pub fn main() !void {
    var sum : i64 = 0;

    // convert and sum 
    var vals = split(u8, data, "\n");
    while (vals.next()) |value| {
        sum += parseInt(i64, value, 10) catch 0; // empty string
    }
    print("Part 1: {}", .{sum});

    // part 2
    vals.reset();
    var arr_size = 1000;
    const seen = gpa.alloc(i64, arr_size);

    while (true) {

    }
    _ = seen;
    

}

// Useful stdlib functions
const tokenize = std.mem.tokenize;
const split = std.mem.splitSequence;
const indexOf = std.mem.indexOfScalar;
const indexOfAny = std.mem.indexOfAny;
const indexOfStr = std.mem.indexOfPosLinear;
const lastIndexOf = std.mem.lastIndexOfScalar;
const lastIndexOfAny = std.mem.lastIndexOfAny;
const lastIndexOfStr = std.mem.lastIndexOfLinear;
const trim = std.mem.trim;
const sliceMin = std.mem.min;
const sliceMax = std.mem.max;

const parseInt = std.fmt.parseInt;
const parseFloat = std.fmt.parseFloat;

const min = std.math.min;
const min3 = std.math.min3;
const max = std.math.max;
const max3 = std.math.max3;

const print = std.debug.print;
const assert = std.debug.assert;

const sort = std.sort.sort;
const asc = std.sort.asc;
const desc = std.sort.desc;


// Generated from template/template.zig.
// Run `zig build generate` to update.
// Only unmodified days will be updated.
