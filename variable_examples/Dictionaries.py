student_1 = {
    "name": "Susan",
    "stream": "tech",
    "Completed lessons": 4,
    "completed lesson names": ["variables", "data types", "lists and tuples"],
    "passport info": {"passport number": "54809097",
                      "expiry date": "21/09/23"},
    "Car Info": {"CarType": "toyota"}
    }

student_1["Full Name"] = student_1.pop("name")

print(student_1["Full Name"])