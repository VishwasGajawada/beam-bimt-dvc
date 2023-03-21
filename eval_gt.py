import torch

cap_model_cpt = torch.load('./sample/best_cap_model.pt', map_location='cpu')
print(cap_model_cpt['val_1_metrics'])
print(cap_model_cpt['val_2_metrics'])
# To obtain the final results, average values in both dicts