package main

import (
	"errors"
	"fmt"
	"math"
)

type person struct {
	name string
	age int
}

func main() {
	var x int = 5
	var y int = 7
	var sum1 int = x + y

	if sum1 > 10 {
		fmt.Println("more than 10")
	} else if sum1 > 20 {
		fmt.Println("more than 20")
	} else {
		fmt.Println("less than 10")
	}

	fmt.Println(sum1)

	//arrays
	var a[5] int
	a[2] = 7
	fmt.Println(a)

	b := [5]int{1,2,3,4,5}
	fmt.Println(b)

	//slices
	sliceA := []int{}
	sliceA = append(sliceA,3)
	fmt.Println(sliceA)
	
	//map
	vertices := make(map[string]int)
	vertices["triangle"] = 3
	vertices["square"] = 4
	vertices["dodecagon"] = 12

	delete(vertices, "triangle")
	fmt.Println(vertices)

	//loop
	for i:= 0; i < 5; i++ {
		fmt.Println(i)
	}

	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}

	arr := []string{"a", "b", "c", "d", "e", "f"}
	for index, value := range arr {
		fmt.Println("index", index, "value", value)
	}

	m := make(map[string]string)
	m["a"] = "alpha"
	m["b"] = "beta"
	for key, value := range m {
		fmt.Println("key", key, "value", value)
	}

	//functions
	result := sum(2, 3)
	fmt.Println(result)

	result1, err := sqrt(16)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result1)
	}
	
	//struct
	p := person{name: "John", age: 23}
	fmt.Println(p)


	//pointers
	v := 7
	fmt.Println(v)
	fmt.Println(&v)
	inc(&v)
	fmt.Println(v)

}

func sum(x int, y int) int {
	return x + y
}

func sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, errors.New("Undefined for negative numbers")
	}
	return math.Sqrt(x), nil
}

func inc(x *int) {
	*x++
}