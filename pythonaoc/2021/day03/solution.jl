inp = open(f->read(f, String),"2021/day03/input.txt","r")
byt_str =  split(inp,"\n")

function find_common(list, idx, bias)
    x, y = 0, 0
    for i in list
        if i[idx] == bias
            x += 1
        else 
            y += 1
        end
    end
    if x > y
        return "1"
    elseif y>x
        return "0"
    else
        return string(bias)
    end
end

gamma = join([find_common(byt_str, i, '1') for i in range(1,length = length(byt_str[1]))])
beta = join([find_common(byt_str, i, '0') for i in range(1,length = length(byt_str[1]))])
gamma = parse(Int, gamma, base=2)
beta = parse(Int, beta, base=2)
println("P1:", gamma*beta)

function find_bit(array, bias)
    for i in 1:length(array[1])
        x = find_common(array, i, bias)
        filter!(z->string(z[i]) == x, array)
        if length(array) <= 1
            return array[1]
            break
        end
    end
    
end
oxy_bits = copy(byt_str)
co2_bits = copy(byt_str)
oxy_rating = parse(Int,find_bit(oxy_bits, '1'),base=2)
co2_rating = parse(Int,find_bit(co2_bits, '0'),base=2)
print("P2:", oxy_rating*co2_rating)