a = {
    0.3: {
        "Bleu_1": 0.20993756,
        "Bleu_2": 0.10860487,
        "Bleu_3": 0.058206131,
        "Bleu_4": 0.028938321,
        "METEOR": 0.1072044739,
        "ROUGE_L": 0.21132889,
        "CIDEr": 0.1443622035,
        "Recall": 0.97504290266,
        "Precision": 0.87441661818,
    },
    0.5: {
        "Bleu_1": 0.187872501,
        "Bleu_2": 0.098267082,
        "Bleu_3": 0.0525296804,
        "Bleu_4": 0.0258714605,
        "METEOR": 0.10453595986,
        "ROUGE_L": 0.182378303,
        "CIDEr": 0.14889081537,
        "Recall": 0.9216620046,
        "Precision": 0.0623122771,
    },
    0.7: {
        "Bleu_1": 0.11881859562,
        "Bleu_2": 0.06283721932,
        "Bleu_3": 0.03316205542,
        "Bleu_4": 0.01613379419,
        "METEOR": 0.08574302544,
        "ROUGE_L": 0.05838264441272359,
        "CIDEr": 0.06242451440147922,
        "Recall": 0.79584527116,
        "Precision": 0.32965240808,
    },
    0.9: {
        "Bleu_1": 0.016208334498795718,
        "Bleu_2": 0.008192344763173674,
        "Bleu_3": 0.00978045399812,
        "Bleu_4": 0.00434144188608,
        "METEOR": 0.04033038560000002,
        "ROUGE_L": 0.017591190443169903,
        "CIDEr": 0.058504590289,
        "Recall": 0.519921310998,
        "Precision": 0.1020443721,
    },
    "Average across tIoUs": {
        "Bleu_1": 0.13320924777969895,
        "Bleu_2": 0.06947537902079343,
        "Bleu_3": 0.03841958020453,
        "Bleu_4": 0.01882125439402,
        "METEOR": 0.08445346120000001,
        "ROUGE_L": 0.11742025696397337,
        "CIDEr": 0.10354553089011981,
        "Recall": 0.8031178723545,
        "Precision": 0.342106418865,
    },
}


# Get the keys in the inner dictionary
metric_keys = a[0.3].keys()

# Calculate the average for each metric across tIoUs
averages = {}
for metric_key in metric_keys:
    # Calculate the average of the metric across tIoUs
    metric_total = sum(a[tIoU][metric_key] for tIoU in a)
    metric_avg = metric_total / len(a)
    
    # Add the average to the dictionary
    averages[metric_key] = metric_avg

# Add the new key-value pair to the variable a
a["Average across tIoUs"] = averages


print(a)