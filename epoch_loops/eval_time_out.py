max_len = 30
start_idx = 2
end_idx = 3
pad_idx = 1
initial beams = [{'sequence': tensor([[2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2],
        [2]], device='cuda:0'), 'score': tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       device='cuda:0')}]
[{'sequence': tensor([[ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  4],
        [ 2, 36],
        [ 2,  4],
        [ 2, 32],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  5],
        [ 2, 23],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2, 36],
        [ 2, 18],
        [ 2,  5],
        [ 2,  5],
        [ 2, 36],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2, 23],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  4],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2,  5],
        [ 2, 18],
        [ 2,  5],
        [ 2,  5],
        [ 2, 18],
        [ 2,  5]], device='cuda:0'), 'score': tensor([-1.4062, -1.5585, -2.2565, -2.3166, -2.4607, -2.5224, -2.5880, -2.2704,
        -2.3722, -1.2573, -2.0505, -2.3947, -2.6542, -1.9588, -2.2315, -1.5255,
        -1.8318, -1.1879, -2.0971, -2.1822, -1.7855, -1.9781, -1.4328, -2.0339,
        -2.2511, -1.4305, -2.1577, -2.2558, -2.3538, -1.4147, -1.5924, -2.1186,
        -1.3428, -1.9749, -1.7681, -2.2079, -2.1922, -1.4216, -2.1498, -1.8404,
        -2.4910, -1.3078, -2.0954, -1.8993, -1.9509, -1.5930, -1.8060, -2.5106,
        -2.5800, -2.0191, -2.2722, -1.6133, -1.9230, -2.2754, -2.7080, -1.8341,
        -1.9230, -1.6342, -2.2106, -2.6281, -1.8313, -1.6801, -2.3563, -1.6598],
       device='cuda:0', grad_fn=<AddBackward0>)}, {'sequence': tensor([[  2,   4],
        [  2,  18],
        [  2,  32],
        [  2,  32],
        [  2,   5],
        [  2,   5],
        [  2, 177],
        [  2,  32],
        [  2,   4],
        [  2,  35],
        [  2,   5],
        [  2,  39],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,  18],
        [  2,  35],
        [  2,  23],
        [  2,  18],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,  23],
        [  2,   5],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,  23],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,  35],
        [  2,  39],
        [  2,   5],
        [  2,   5],
        [  2,   4],
        [  2,   4],
        [  2,   5],
        [  2,  45],
        [  2,   4],
        [  2,  35],
        [  2,  18],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,   4],
        [  2,  39],
        [  2,  17],
        [  2,  39],
        [  2,   4],
        [  2,   4],
        [  2,  36],
        [  2,  18],
        [  2,   5],
        [  2,   4],
        [  2,  35],
        [  2,  35],
        [  2,  39],
        [  2,   4],
        [  2,   4],
        [  2,  35],
        [  2,  45],
        [  2,  35]], device='cuda:0'), 'score': tensor([-4.4881, -4.0860, -3.4148, -3.1749, -2.5495, -2.8587, -3.0678, -3.1674,
        -2.6540, -4.6131, -2.6364, -2.5267, -2.8909, -2.9408, -2.7444, -4.1584,
        -3.1046, -4.1017, -2.3322, -3.5117, -3.1921, -3.1914, -4.5996, -2.6139,
        -2.2938, -4.8237, -2.4513, -3.0015, -3.3392, -4.7042, -2.1181, -2.8070,
        -4.2475, -3.6415, -2.2769, -2.7817, -2.9102, -4.6570, -2.5250, -3.1800,
        -3.3529, -4.4888, -2.7278, -2.7539, -3.1643, -3.8221, -3.0469, -3.4181,
        -2.6083, -2.8608, -2.5594, -4.1311, -3.1083, -3.3862, -2.8935, -3.8971,
        -3.5443, -3.5510, -3.1563, -3.1001, -2.7762, -4.3358, -3.7876, -4.1828],
       device='cuda:0', grad_fn=<AddBackward0>)}]