def findDecision(obj): #obj[0]: ECR_RATIO, obj[1]: MVL SUM, obj[2]: MVL ABS, obj[3]: RMS, obj[4]: DB, obj[5]: ZCR, obj[6]: MFCC, obj[7]: FARBWECHSEL RATIO, obj[8]: SIFT RATIO, obj[9]: Tag, obj[10]: Zeit
   # {"feature": "SIFT RATIO", "instances": 106, "metric_value": 0.2508, "depth": 1}
   if obj[8]<=0.3398845709363958:
      return 0
   elif obj[8]>0.3398845709363958:
      # {"feature": "DB", "instances": 14, "metric_value": 0.4103, "depth": 2}
      if obj[4]<=-32.21442271726036:
         return 1
      elif obj[4]>-32.21442271726036:
         return 0
      else:
         return 0.0
   else:
      return 0.7857142857142857
