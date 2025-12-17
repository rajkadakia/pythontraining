import numpy as np

demand = np.array([120, 135, 140, 0, 145,-20, 150, 155, 1000, 160,165, 0, 170, 175, 180])

print(demand)
print(demand.shape)
demand_clean = np.where(demand<0,0,demand)
print(demand_clean)

demand_nonzero=demand_clean[demand_clean>0]
print(demand_nonzero)
print(demand_nonzero.shape)

mean=np.mean(demand_nonzero)
std=np.std(demand_nonzero)
print(mean)
print(std)
limit = mean+2*std
print(limit)

demand_capped=np.where(demand_nonzero>limit,limit,demand_nonzero)
print(demand_capped)
min = np.min(demand_capped)
max=np.max(demand_capped)
print(min,max)
demand_norm=((demand_capped-min)/(max-min))
print(demand_norm)
print(demand_norm.shape)
window = 7
rolling_avg = np.array([
    np.mean(demand_norm[i:i+window])
    for i in range(len(demand_norm) - window + 1)
])

print(rolling_avg)
print(rolling_avg.shape)
threshold = np.percentile(demand_norm, 80)
top_days = demand_norm[demand_norm >= threshold]

print("Threshold:", threshold)
print("Top 20% demand days:", top_days)

cumulative = np.cumsum(demand_norm)
print(cumulative)

daily_growth = np.diff(demand_norm)
avg_growth = np.mean(daily_growth)

print("Average daily growth:", avg_growth)

weekly_demand = demand_norm.reshape(2, 6)

print(weekly_demand)
print(weekly_demand.shape)
