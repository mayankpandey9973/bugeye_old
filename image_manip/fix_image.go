package main

import (
    "fmt"
    "os"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

    f, err := os.Open("imagepos_raw.txt")
    check(err)

    fmt.Printf("Imagepos = [None]*100\n")
    for i:=0; i<100; i++ {
    	var x, y int
	fmt.Fscanf(f,"%d %d", &x, &y)
	fmt.Printf("Imagepos[%d] = [%d,%d]\n",i, x*2, y*3/2)
    }	

    f.Close()

}
