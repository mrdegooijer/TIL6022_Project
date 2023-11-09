import matplotlib.pyplot as plt
from delay_visualization import train_info_dict
from delay_visualization import traintype

delayed_trains_times = [train_info_dict[train_id]["delay"]/60 for train_id in range(len(traintype))]

color_map = {'IC': 'blue', 'spr': 'greenyellow'}
train_colors = [color_map[train_info_dict[train_id]['type']] for train_id in range(len(traintype))]

delayed_train_indices = [train_id for train_id in range(len(traintype))]

# Use the delayed train indices and their corresponding colors to create a bar chart
plt.bar([delayed_train_indices.index(i) for i in range(len(delayed_train_indices))], [delayed_trains_times[i] for i in delayed_train_indices], color=[train_colors[i] for i in delayed_train_indices])
# plt.bar(range(len(delayed_trains_times)), delayed_trains_times)

plt.axhline(0, color='red', linestyle='--')

plt.xlabel('Train Index')
plt.ylabel('Delay (minutes)')
plt.title('Delays of Trains')

legend_labels = {'IC': 'Intercity (IC)', 'spr': 'Sprinter (spr)'}
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=color_map[train_type]) for train_type in color_map]
plt.legend(legend_handles, [legend_labels[train_type] for train_type in legend_labels])

plt.show()
