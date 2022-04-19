package main

import (
	"fmt"
	"io"
	"log"
	"os"

	flatbuffers "github.com/google/flatbuffers/go"

	schema "test.com/test"
)

func send_fb_file(filename string, output_filename string) {
	// 20 MB:
	read_size := 20000000
	//read_size := 20000

	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	output, err := os.OpenFile(output_filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)

	if err != nil {
		log.Fatal(err)
	}

	// what does check do idk
	//check(err)

	packet_count := 0
	bytes := make([]byte, read_size)
	for {
		amount_read, err := file.Read(bytes)

		if err != nil {
			if err == io.EOF {
				break
			}
			log.Fatal(err)
		}

		// do something with read bytes:
		debug_use_flatbuffer(bytes[0:amount_read], filename, output, packet_count)

		packet_count += 1
	}

}

func debug_use_flatbuffer(bytes []byte, filename string, output_file *os.File, packet_count int) {

	// check (if bytes empty) -> true
	output := build_flatbuffer(bytes, filename, packet_count, false)

	// get contents from flatbuffer
	fb_file := schema.GetRootAsFile(output, 0)
	name := fb_file.Filename()
	nr := fb_file.Packetnumber()
	eof := fb_file.Eof()

	fmt.Println(name, nr, eof)

	/*
		arr := make([]byte, fb_file.DataLength())
		for i := 0; i < fb_file.DataLength(); i++ {
			arr[i] = byte(fb_file.Data(i))
		}*/

	arr := fb_file.DataBytes()

	// save arr to output file
	output_file.Write(arr)

	//err := ioutil.WriteFile(output_filename, arr, 0644)

	/*
		if err != nil {
			log.Fatal(err)
		}*/
}

func build_flatbuffer(bytes []byte, filename string, packet_count int, eof bool) []byte {
	builder := flatbuffers.NewBuilder(0)
	fname := builder.CreateString(filename)
	arr := builder.CreateByteVector(bytes)

	schema.FileStart(builder)
	schema.FileAddFilename(builder, fname)
	schema.FileAddPacketnumber(builder, int32(packet_count))
	schema.FileAddEof(builder, eof)
	schema.FileAddData(builder, arr)
	binFile := schema.FileEnd(builder)

	builder.Finish(binFile)

	return builder.FinishedBytes()
}

func write_file(arr []byte, filename string) {
	// save all bytes in Data array to arr
	// for i := 0; i < test.DataLength(); i++ {
	// 	arr[i] = byte(test.Data(i))
	// }

	// // save arr to file "hellgo.png"
	// err := ioutil.WriteFile("hellgo.png", arr, 0644)
}

func main() {
	send_fb_file("portal2.zip", "ouputCOOL.zip")
	//send_fb_file("hellgo.png", "HELLLLLL.png")
}