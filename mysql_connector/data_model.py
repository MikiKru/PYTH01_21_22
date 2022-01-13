class DataModel:
    def __init__(self, METER_ID, METER_OBJECT_ID, CAP_TIME, ACQ_TIME, FLAGS, SCALE, UNIT, REASON, VALUE, USER_ID, DATA, DEP_TIME, EXPRESSION):
        self.meter_id = METER_ID
        self.meter_object_id = METER_OBJECT_ID
        self.cap_time = CAP_TIME
        self.acq_time = ACQ_TIME
        self.flags = FLAGS
        self.scale = SCALE
        self.unit = UNIT
        self.reason = REASON
        self.value = VALUE
        self.user_id = USER_ID
        self.data = DATA
        self.dep_time = DEP_TIME
        self.expression = EXPRESSION