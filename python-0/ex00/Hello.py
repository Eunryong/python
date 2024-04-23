
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list.pop()
ft_list.append("World!")

ft_tuple = list(ft_tuple)
ft_tuple.pop()
ft_tuple.append("Korea!")
ft_tuple = tuple(ft_tuple)

ft_set.remove("tutu!")
# ft_set.discard("tutu!")
ft_set.add("Seoul!")

ft_dict["Hello"] = "42Seoul!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
