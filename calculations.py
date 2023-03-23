import numpy as np

#Function to check the time between the requests in each chunk and calculate the mean
def calc_avg_timediff(userdata):
    #We get a list of all timestamps within the data chunk
    timestamps = userdata['timestamp'].tolist()
    timestamps = np.array(timestamps)
    
    #calculates the avarage in milliseconds
    avg_ms = np.average(np.diff(timestamps))
    
    return avg_ms/1000