# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Task(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Task()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTask(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Task
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Task
    def Hardware(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from schema.Hardware import Hardware
            obj = Hardware()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Task
    def Stages(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from schema.Stage import Stage
            obj = Stage()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Task
    def StagesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Task
    def StagesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Task
    def Artifacts(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Task
    def ArtifactsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Task
    def ArtifactsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def TaskStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddHardware(builder, hardware): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(hardware), 0)
def TaskAddHardware(builder, hardware):
    """This method is deprecated. Please switch to AddHardware."""
    return AddHardware(builder, hardware)
def AddStages(builder, stages): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(stages), 0)
def TaskAddStages(builder, stages):
    """This method is deprecated. Please switch to AddStages."""
    return AddStages(builder, stages)
def StartStagesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TaskStartStagesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStagesVector(builder, numElems)
def AddArtifacts(builder, artifacts): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(artifacts), 0)
def TaskAddArtifacts(builder, artifacts):
    """This method is deprecated. Please switch to AddArtifacts."""
    return AddArtifacts(builder, artifacts)
def StartArtifactsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TaskStartArtifactsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartArtifactsVector(builder, numElems)
def End(builder): return builder.EndObject()
def TaskEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)