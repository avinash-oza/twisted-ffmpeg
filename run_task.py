from celery_task import encode_video
 
 
test1 = "/DVR/172.16.1.46/CH1/20140416/014329-014505.avi"
test2 = "/DVR/172.16.1.46/CH1/20140416/034414-041414.avi"
encode_video.delay(test1, "output1.avi")
#encode_video.delay(test2, "output2.avi")

