# import torch

# # create sample data with 64 arrays, each containing k dictionaries
# k = 2
# data = []
# for i in range(5):
#     arr = []
#     for j in range(k):
#         sequence = torch.rand(10)
#         score = torch.rand(1).item()
#         candidate = {"sequence": sequence, "score": score}
#         arr.append(candidate)
#     data.append(arr)

# print("data = ", data)
# # concatenate the "sequence" and "score" arrays for each dictionary across all 64 arrays
# output = []
# for i in range(k):
#     # sequence_concat = torch.cat([d[i]["sequence"] for d in data])
#     sequence_concat = torch.cat([d[i]["sequence"].unsqueeze(0) for d in data], dim=0)
#     score_concat = torch.tensor([d[i]["score"] for d in data])
#     output.append({"sequence": sequence_concat, "score": score_concat})

# # print the output array
# print(output)

