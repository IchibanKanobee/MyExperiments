package main

import "fmt"

func main() {
	var conferenceName = "Go Conference"
	const conferenceTickets uint = 50
	var remainingTickets = conferenceTickets

	fmt.Printf("conferenceName is %T, remainingTickets is %T, remainingTickets is %T\n", conferenceName, remainingTickets, conferenceTickets)

	fmt.Printf("Welcome to %v booking application\n", conferenceName)
	fmt.Printf("We have total of %v tickets and %v are available\n", conferenceTickets, remainingTickets)
	fmt.Println("Get your tickets here to attend")

	var firstName string
	var lastName string
	var email string
	var userTickets uint

	var bookings = [50] string {}

	fmt.Println("Enter your first name:")
	fmt.Scan(&firstName)
	
	fmt.Println("Enter your last name:")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email:")
	fmt.Scan(&email)

	fmt.Println("Enter number of tickets:")
	fmt.Scan(&userTickets)

	bookings[0] = firstName + "" + lastName
	fmt.Println("The whole array %v", bookings)
	fmt.Println("The first element %v", bookings[0])
	fmt.Println("Array type %T", bookings)
	fmt.Println("Array length %v", len(bookings))



	remainingTickets = remainingTickets - userTickets
	fmt.Printf("Thank you %v %v for booking %v tickets. You will receive a confirmation email at %v\n", firstName, lastName, userTickets, email)
	fmt.Printf("%v tickets are remaining for %v\n", remainingTickets, conferenceName)
}
