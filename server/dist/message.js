"use strict";
// automatically generated by the FlatBuffers compiler, do not modify
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const flatbuffers = __importStar(require("flatbuffers"));
class Message {
    constructor() {
        this.bb = null;
        this.bb_pos = 0;
    }
    __init(i, bb) {
        this.bb_pos = i;
        this.bb = bb;
        return this;
    }
    static getRootAsMessage(bb, obj) {
        return (obj || new Message()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
    }
    static getSizePrefixedRootAsMessage(bb, obj) {
        bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
        return (obj || new Message()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
    }
    agentId() {
        const offset = this.bb.__offset(this.bb_pos, 4);
        return offset ? this.bb.readInt32(this.bb_pos + offset) : 0;
    }
    cmd(optionalEncoding) {
        const offset = this.bb.__offset(this.bb_pos, 6);
        return offset ? this.bb.__string(this.bb_pos + offset, optionalEncoding) : null;
    }
    data(index) {
        const offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? this.bb.readInt8(this.bb.__vector(this.bb_pos + offset) + index) : 0;
    }
    dataLength() {
        const offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? this.bb.__vector_len(this.bb_pos + offset) : 0;
    }
    dataArray() {
        const offset = this.bb.__offset(this.bb_pos, 8);
        return offset ? new Int8Array(this.bb.bytes().buffer, this.bb.bytes().byteOffset + this.bb.__vector(this.bb_pos + offset), this.bb.__vector_len(this.bb_pos + offset)) : null;
    }
    static startMessage(builder) {
        builder.startObject(3);
    }
    static addAgentId(builder, agentId) {
        builder.addFieldInt32(0, agentId, 0);
    }
    static addCmd(builder, cmdOffset) {
        builder.addFieldOffset(1, cmdOffset, 0);
    }
    static addData(builder, dataOffset) {
        builder.addFieldOffset(2, dataOffset, 0);
    }
    static createDataVector(builder, data) {
        builder.startVector(1, data.length, 1);
        for (let i = data.length - 1; i >= 0; i--) {
            builder.addInt8(data[i]);
        }
        return builder.endVector();
    }
    static startDataVector(builder, numElems) {
        builder.startVector(1, numElems, 1);
    }
    static endMessage(builder) {
        const offset = builder.endObject();
        return offset;
    }
    static finishMessageBuffer(builder, offset) {
        builder.finish(offset);
    }
    static finishSizePrefixedMessageBuffer(builder, offset) {
        builder.finish(offset, undefined, true);
    }
    static createMessage(builder, agentId, cmdOffset, dataOffset) {
        Message.startMessage(builder);
        Message.addAgentId(builder, agentId);
        Message.addCmd(builder, cmdOffset);
        Message.addData(builder, dataOffset);
        return Message.endMessage(builder);
    }
}
exports.Message = Message;
