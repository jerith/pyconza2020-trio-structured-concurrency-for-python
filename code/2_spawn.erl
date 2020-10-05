%% This is a recursive function with two clauses.
%% It counts backwards because that's less code.
say(_, 0) ->
    ok;
say(Msg, N) ->
    io:fwrite("~w ~s~n", [N, Msg]),
    timer:sleep(200),
    say(Msg, N-1).

main(_) ->
    spawn(fun() -> say("task1", 5) end),
    spawn(fun() -> say("task2", 5) end),
    timer:sleep(1100).
