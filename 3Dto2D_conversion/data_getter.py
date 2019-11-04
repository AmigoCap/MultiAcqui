import pandas as pd
import numpy as np

import json

from os import walk
from os.path import join


# note : we need a synch frame that we know happens at the same time on mocap and video.
# here for 3d data, it's frame 557 and for 2d data it's frame 173

# also, we need a framerate ratio : mocap_framerate/gopro_framerate
# here, it's about 9 (hence the num%9 in get_3d_data)


def get_3d_data () :
    mocap_data_path = "../211019_NicoGabin_carre/211019_NicoGabin_MoCapCarre-Copie.csv"
    df_mocap = pd.read_csv(mocap_data_path, sep=',', index_col=[0], header=[0,1]) 
    segments=['Nico1:epd1','Nico1:epd2','Nico1:bd2','Nico1:abg1','Nico1:abd2','Nico1:abg2']
    coord_3d_list = []
    for num in range(557, 1497) :
        coord_3d=[]
        if num%9==0 :
            for seg in segments:
                data=df_mocap[seg].iloc[num]
                articulation_coord = np.array([[data.X],[data.Y],[data.Z]])
                coord_3d.append(articulation_coord)
            coord_3d_list.append(coord_3d)
    return coord_3d_list
    
    
    
def get_2d_data () :
    relative_path = "../211019_NicoGabin_carre/OpenPose_skellington_capture/"
    data=[]
    for root, dirs, files in walk(relative_path, topdown=True) :
        files.sort()
        for file in files :
            jsonfile = join(root, file)
            if not jsonfile.endswith('.json') : continue
            with open(jsonfile) as file:
                people=json.loads(file.read())['people'][0]['pose_keypoints_2d']
                data.append(people)
    iterables=[["Nose","Neck","RShoulder","RElbow","RWrist","LShoulder","LElbow","LWrist","RHip","RKnee","RAnkle","LHip","LKnee","LAnkle","REye","LEye","REar","LEar"],['x','y','c']]
    columns=pd.MultiIndex.from_product(iterables, names=['first', 'second'])
    df_openpose=pd.DataFrame(data, columns=columns)

    segments=['RShoulder','LShoulder',"RElbow","LElbow","RWrist","LWrist"]
    coord_2d_list = []
    for num in range(173, 450) :
        coord_2d=[]
        for seg in segments:
            data=df_openpose[seg].iloc[num]
            articulation_coord = np.array([[data.x],[data.y]])
            coord_2d.append(articulation_coord)
        coord_2d_list.append(coord_2d)
    return coord_2d_list
