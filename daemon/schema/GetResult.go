// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package schema

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type GetResult struct {
	_tab flatbuffers.Table
}

func GetRootAsGetResult(buf []byte, offset flatbuffers.UOffsetT) *GetResult {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &GetResult{}
	x.Init(buf, n+offset)
	return x
}

func GetSizePrefixedRootAsGetResult(buf []byte, offset flatbuffers.UOffsetT) *GetResult {
	n := flatbuffers.GetUOffsetT(buf[offset+flatbuffers.SizeUint32:])
	x := &GetResult{}
	x.Init(buf, n+offset+flatbuffers.SizeUint32)
	return x
}

func (rcv *GetResult) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *GetResult) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *GetResult) IdList(j int) []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		a := rcv._tab.Vector(o)
		return rcv._tab.ByteVector(a + flatbuffers.UOffsetT(j*4))
	}
	return nil
}

func (rcv *GetResult) IdListLength() int {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.VectorLen(o)
	}
	return 0
}

func GetResultStart(builder *flatbuffers.Builder) {
	builder.StartObject(1)
}
func GetResultAddIdList(builder *flatbuffers.Builder, idList flatbuffers.UOffsetT) {
	builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(idList), 0)
}
func GetResultStartIdListVector(builder *flatbuffers.Builder, numElems int) flatbuffers.UOffsetT {
	return builder.StartVector(4, numElems, 4)
}
func GetResultEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}
