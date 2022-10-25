#!usr/bin/env python3

# Here are some font ligatures!
# www **  *** **/ *>  */   \\\\ \\\\\\   {- ::
# ::: :=  !!  !=  !== -}   ---- -->  ->  ->>
# -<  -<< -~  #{  #[  ##   ###  #### #(  #? #_
# #_( .- .= . . . .< ...   ?=   ??   ;;  /* /**
# /=  /== />  //  /// &&   ||   ||=  |=  |> ^= $>
# ++  +++ +>  =:= ==  ===  ==>  =>   =>> <=
# =<< =/= >-  >=  >=> >>   >>-  >>=  >>> <*
# <*> <|  <|> <$  <$> <!-- <-   <--  <-> <+
# <+> <=  <== <=> <=< <>   <<   <<-  <<= <<<
# <~  <~~ </  </> ~@  ~-   ~>   ~~   ~~> %%
# 0x0 600x800 <>


def function(x, y):
    return x + y


def equals_number(x, y):
    return x == y


def configurable_wrapper(var):
    def wrapper(fn):
        def inner(*args, **kwargs):
            print(f"Variable is: {var}")

        return inner

    return wrapper


en_lambda = lambda x, y: equals_number(x, y)  # -> Shorter option!


class Class:
    @configurable_wrapper("My class!")
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    myClass = Class()
