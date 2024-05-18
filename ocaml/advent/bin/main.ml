let input = "../../data/2018/day01.txt"


let get_input_from_file path =
  let ic = open_in path in 
    try
      really_input_string ic (in_channel_length ic)
        |> String.split_on_char '\n'
    with e->
      close_in_noerr ic;
      raise e


let () =  
  let inp = get_input_from_file input in 
    Advent.Day1_18.part_one inp
      |> Printf.printf "%n\n";

  Printf.printf "\n%s\n" Advent.Day1_18.v;
  

  let f = get_input_from_file input in 
    List.iter print_endline f
