# knights tour

Small program that takes three user inputs, first the board size that will be used for the kngiht's tour, the second and third are the columns and row respectively from which the knigth will start the tour, starting at 0. The knight will prioritize moving to a square that has the least legal moves available (Warnsdorff's rule
). This speeds up the runtime considerably, currently the maximun board size is around 45 x 45 the runtime is still very fast (less than 0.5 seconds) but the program crashes due to using a lot of memory.
