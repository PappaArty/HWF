# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Result(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Result()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsResult(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Result
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Result
    def Time(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Result
    def Stages(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from schema.StageResult import StageResult
            obj = StageResult()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Result
    def StagesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Result
    def StagesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Result
    def Artifacts(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from schema.Artifact import Artifact
            obj = Artifact()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Result
    def ArtifactsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Result
    def ArtifactsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Result
    def Hardware(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from schema.Hardware import Hardware
            obj = Hardware()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Result
    def HardwareLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Result
    def HardwareIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def ResultStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTime(builder, time): builder.PrependInt32Slot(0, time, 0)
def ResultAddTime(builder, time):
    """This method is deprecated. Please switch to AddTime."""
    return AddTime(builder, time)
def AddStages(builder, stages): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(stages), 0)
def ResultAddStages(builder, stages):
    """This method is deprecated. Please switch to AddStages."""
    return AddStages(builder, stages)
def StartStagesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ResultStartStagesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStagesVector(builder, numElems)
def AddArtifacts(builder, artifacts): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(artifacts), 0)
def ResultAddArtifacts(builder, artifacts):
    """This method is deprecated. Please switch to AddArtifacts."""
    return AddArtifacts(builder, artifacts)
def StartArtifactsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ResultStartArtifactsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartArtifactsVector(builder, numElems)
def AddHardware(builder, hardware): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(hardware), 0)
def ResultAddHardware(builder, hardware):
    """This method is deprecated. Please switch to AddHardware."""
    return AddHardware(builder, hardware)
def StartHardwareVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ResultStartHardwareVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartHardwareVector(builder, numElems)
def End(builder): return builder.EndObject()
def ResultEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)