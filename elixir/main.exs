# Entry point for 
defmodule Day1 do
  def part_one(inp) do
    parse_input(inp)
      |> Enum.reduce(0, fn x, acc -> x + acc end)
  end

  def part_two(inp) do
    parse_input(inp)
      |> Stream.cycle()
      |> Enum.reduce_while({0, MapSet.new([0])}, fn move, {current, seen} -> 
        new = current + move
        cond do
          MapSet.member?(seen, new) -> {:halt, new}
          true -> {:cont, {new, MapSet.put(seen, new)}}
        end
    end)
  end

  def parse_input(inp) do
    String.split(inp, "\n", trim: true)
     |>  Enum.map(fn x -> String.to_integer(x) end)
  end

end

data = File.read!("input.txt")

IO.puts Day1.part_one(data)
IO.puts Day1.part_two(data)



