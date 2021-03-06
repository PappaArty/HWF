# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class File(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = File()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFile(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # File
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # File
    def Filename(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # File
    def Packetnumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # File
    def Eof(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # File
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # File
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # File
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # File
    def DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def FileStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFilename(builder, filename): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(filename), 0)
def FileAddFilename(builder, filename):
    """This method is deprecated. Please switch to AddFilename."""
    return AddFilename(builder, filename)
def AddPacketnumber(builder, packetnumber): builder.PrependInt32Slot(1, packetnumber, 0)
def FileAddPacketnumber(builder, packetnumber):
    """This method is deprecated. Please switch to AddPacketnumber."""
    return AddPacketnumber(builder, packetnumber)
def AddEof(builder, eof): builder.PrependBoolSlot(2, eof, 0)
def FileAddEof(builder, eof):
    """This method is deprecated. Please switch to AddEof."""
    return AddEof(builder, eof)
def AddData(builder, data): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def FileAddData(builder, data):
    """This method is deprecated. Please switch to AddData."""
    return AddData(builder, data)
def StartDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def FileStartDataVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDataVector(builder, numElems)
def End(builder): return builder.EndObject()
def FileEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)