"use strict";
// automatically generated by the FlatBuffers compiler, do not modify
Object.defineProperty(exports, "__esModule", { value: true });
exports.Message = void 0;
/**
 * @constructor
 */
class Message {
    constructor() {
        this.bb = null;
        this.bb_pos = 0;
    }
    /**
     * @param number i
     * @param flatbuffers.ByteBuffer bb
     * @returns Message
     */
    __init(i, bb) {
        this.bb_pos = i;
        this.bb = bb;
        return this;
    }
    ;
    /**
     * @param flatbuffers.ByteBuffer bb
     * @param Message= obj
     * @returns Message
     */
    static getRootAsMessage(bb, obj) {
        return (obj || new Message).__init(bb.readInt32(bb.position()) + bb.position(), bb);
    }
    ;
    agentId(optionalEncoding) {
        var offset = this.bb.__offset(this.bb_pos, 4);
        return offset ? this.bb.__string(this.bb_pos + offset, optionalEncoding) : null;
    }
    ;
    cmd(index, optionalEncoding) {
        var offset = this.bb.__offset(this.bb_pos, 6);
        return offset ? this.bb.__string(this.bb.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
    }
    ;
    /**
     * @returns number
     */
    cmdLength() {
        var offset = this.bb.__offset(this.bb_pos, 6);
        return offset ? this.bb.__vector_len(this.bb_pos + offset) : 0;
    }
    ;
    /**
     * @param number index
     * @returns number
     */
    data(index) {
        var offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? this.bb.readInt8(this.bb.__vector(this.bb_pos + offset) + index) : 0;
    }
    ;
    /**
     * @returns number
     */
    dataLength() {
        var offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? this.bb.__vector_len(this.bb_pos + offset) : 0;
    }
    ;
    /**
     * @returns Int8Array
     */
    dataArray() {
        var offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? new Int8Array(this.bb.bytes().buffer, this.bb.bytes().byteOffset + this.bb.__vector(this.bb_pos + offset), this.bb.__vector_len(this.bb_pos + offset)) : null;
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     */
    static startMessage(builder) {
        builder.startObject(3);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param flatbuffers.Offset agentIdOffset
     */
    static addAgentId(builder, agentIdOffset) {
        builder.addFieldOffset(0, agentIdOffset, 0);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param flatbuffers.Offset cmdOffset
     */
    static addCmd(builder, cmdOffset) {
        builder.addFieldOffset(1, cmdOffset, 0);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param Array.<flatbuffers.Offset> data
     * @returns flatbuffers.Offset
     */
    static createCmdVector(builder, data) {
        builder.startVector(4, data.length, 4);
        for (var i = data.length - 1; i >= 0; i--) {
            builder.addOffset(data[i]);
        }
        return builder.endVector();
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param number numElems
     */
    static startCmdVector(builder, numElems) {
        builder.startVector(4, numElems, 4);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param flatbuffers.Offset dataOffset
     */
    static addData(builder, dataOffset) {
        builder.addFieldOffset(2, dataOffset, 0);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param Array.<number> data
     * @returns flatbuffers.Offset
     */
    static createDataVector(builder, data) {
        builder.startVector(1, data.length, 1);
        for (var i = data.length - 1; i >= 0; i--) {
            builder.addInt8(data[i]);
        }
        return builder.endVector();
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param number numElems
     */
    static startDataVector(builder, numElems) {
        builder.startVector(1, numElems, 1);
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @returns flatbuffers.Offset
     */
    static endMessage(builder) {
        var offset = builder.endObject();
        return offset;
    }
    ;
    /**
     * @param flatbuffers.Builder builder
     * @param flatbuffers.Offset offset
     */
    static finishMessageBuffer(builder, offset) {
        builder.finish(offset);
    }
    ;
    static createMessage(builder, agentIdOffset, cmdOffset, dataOffset) {
        Message.startMessage(builder);
        Message.addAgentId(builder, agentIdOffset);
        Message.addCmd(builder, cmdOffset);
        Message.addData(builder, dataOffset);
        return Message.endMessage(builder);
    }
}
exports.Message = Message;