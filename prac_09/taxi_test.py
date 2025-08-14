from prac_09.taxi import Taxi


def test_taxi():
    my_taxi = Taxi("Pirus", 100)

    my_taxi.drive(40)

    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    distance_driven = my_taxi.drive(100)

    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")


test_taxi()