let v = "hi"

let part_one inp = 
  List.map int_of_string inp
   |> List.fold_left (+) 0
