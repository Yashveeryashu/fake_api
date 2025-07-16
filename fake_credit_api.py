from fastapi import FastAPI
from typing import List
from datetime import date

app = FastAPI(title="Fake Credit Detail API")

# Sample credit data (20 entries)
credit_data = [
    {
        "creditId": f"CRD{str(i).zfill(4)}",
        "customerName": name,
        "creditScore": score,
        "loanAmount": amount,
        "loanType": loan,
        "status": status,
        "issueDate": issue,
        "dueDate": due,
        "bankName": bank,
        "interestRate": rate
    }
    for i, (name, score, amount, loan, status, issue, due, bank, rate) in enumerate([
        ("Ravi Kumar", 720, 500000, "Home Loan", "Approved", "2023-01-10", "2033-01-10", "Bank of India", 7.5),
        ("Sneha Mehta", 680, 300000, "Car Loan", "Pending", "2024-05-20", "2029-05-20", "HDFC Bank", 9.0),
        ("Amit Sharma", 800, 200000, "Personal Loan", "Approved", "2022-07-15", "2027-07-15", "Axis Bank", 10.5),
        ("Neha Verma", 750, 450000, "Education Loan", "Approved", "2021-06-01", "2026-06-01", "SBI", 8.2),
        ("Raj Malhotra", 630, 150000, "Credit Card", "Rejected", "2024-02-11", "2029-02-11", "ICICI Bank", 12.0),
        ("Pooja Singh", 710, 600000, "Home Loan", "Approved", "2023-03-22", "2033-03-22", "PNB", 7.0),
        ("Ankit Jain", 670, 350000, "Car Loan", "Pending", "2023-11-05", "2028-11-05", "HDFC Bank", 9.5),
        ("Rakesh Yadav", 780, 800000, "Home Loan", "Approved", "2020-08-10", "2030-08-10", "SBI", 6.9),
        ("Priya Sharma", 745, 250000, "Personal Loan", "Approved", "2024-01-01", "2029-01-01", "Axis Bank", 10.0),
        ("Nikhil Rathi", 655, 120000, "Credit Card", "Rejected", "2022-10-10", "2027-10-10", "ICICI Bank", 11.5),
        ("Meena Gupta", 695, 400000, "Car Loan", "Approved", "2021-12-20", "2026-12-20", "Kotak Bank", 9.0),
        ("Vikas Dubey", 610, 100000, "Personal Loan", "Pending", "2023-05-01", "2028-05-01", "IDFC Bank", 13.0),
        ("Anjali Rai", 730, 550000, "Home Loan", "Approved", "2022-03-12", "2032-03-12", "SBI", 7.3),
        ("Suresh Kumar", 760, 150000, "Credit Card", "Approved", "2021-01-10", "2026-01-10", "Axis Bank", 12.5),
        ("Rina Das", 690, 300000, "Education Loan", "Pending", "2023-06-14", "2028-06-14", "Bank of Baroda", 8.8),
        ("Harish Rawat", 725, 700000, "Home Loan", "Approved", "2020-09-30", "2030-09-30", "Canara Bank", 6.5),
        ("Payal Mehra", 665, 250000, "Personal Loan", "Pending", "2022-02-22", "2027-02-22", "ICICI Bank", 10.9),
        ("Nitin Chauhan", 785, 800000, "Home Loan", "Approved", "2024-01-15", "2034-01-15", "HDFC Bank", 6.7),
        ("Sonal Jain", 700, 180000, "Car Loan", "Approved", "2023-04-18", "2028-04-18", "SBI", 9.1),
        ("Rohit Aggarwal", 640, 160000, "Credit Card", "Rejected", "2021-05-05", "2026-05-05", "Axis Bank", 11.2)
    ])
]


# Full transaction data
transactions = [
    {"Date": "01-01-2025", "Description": "Opening Balance", "Deposit": 0, "Withdrawal": 0, "Balance": 5000},
    {"Date": "02-01-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7000},
    {"Date": "05-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6750},
    {"Date": "06-01-2025", "Description": "Online Purchase - Amazon Prime", "Deposit": 0, "Withdrawal": 20, "Balance": 6730},
    {"Date": "08-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 500, "Balance": 6230},
    {"Date": "10-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 6030},
    {"Date": "12-01-2025", "Description": "Transfer from Friend - John", "Deposit": 300, "Withdrawal": 0, "Balance": 6330},
    {"Date": "14-01-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 6315},
    {"Date": "15-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 6195},
    {"Date": "17-01-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 400, "Withdrawal": 0, "Balance": 6595},
    {"Date": "18-01-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 250, "Balance": 6345},
    {"Date": "20-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 6145},
    {"Date": "22-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 6015},
    {"Date": "25-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 600, "Balance": 5415},
    {"Date": "28-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 5265},
    {"Date": "30-01-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 100, "Balance": 5165},
    {"Date": "01-02-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7165},
    {"Date": "03-02-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7145},
    {"Date": "04-02-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7245},
    {"Date": "05-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 300, "Balance": 6945},
    {"Date": "07-02-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 6445},
    {"Date": "10-02-2025", "Description": "Transfer from Friend - Lisa", "Deposit": 200, "Withdrawal": 0, "Balance": 6645},
    {"Date": "12-02-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 5945},
    {"Date": "13-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 5695},
    {"Date": "15-02-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 5565},
    {"Date": "18-02-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 500, "Withdrawal": 0, "Balance": 6065},
    {"Date": "20-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 5865},
    {"Date": "22-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 300, "Balance": 5565},
    {"Date": "25-02-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 5765},
    {"Date": "27-02-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 5415},
    {"Date": "01-03-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7415},
    {"Date": "03-03-2025", "Description": "Transfer from Friend - John", "Deposit": 100, "Withdrawal": 0, "Balance": 7515},
    {"Date": "05-03-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7495},
    {"Date": "07-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7345},
    {"Date": "08-03-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7445},
    {"Date": "10-03-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 7430},
    {"Date": "12-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7300},
    {"Date": "14-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 6800},
    {"Date": "17-03-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6550},
    {"Date": "18-03-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 6700},
    {"Date": "20-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 6500},
    {"Date": "22-03-2025", "Description": "Transfer from Friend - John", "Deposit": 250, "Withdrawal": 0, "Balance": 6750},
    {"Date": "25-03-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 6400},
    {"Date": "27-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 6280},
    {"Date": "30-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 5680},
    {"Date": "01-04-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7680},
    {"Date": "03-04-2025", "Description": "Online Purchase - Amazon Prime", "Deposit": 0, "Withdrawal": 20, "Balance": 7660},
    {"Date": "05-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7510},
    {"Date": "07-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 7310},
    {"Date": "10-04-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 200, "Withdrawal": 0, "Balance": 7510},
    {"Date": "12-04-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 300, "Balance": 7210},
    {"Date": "14-04-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 7310},
    {"Date": "15-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7180},
    {"Date": "18-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 6480},
    {"Date": "20-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 250, "Balance": 6230},
    {"Date": "22-04-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 100, "Balance": 6130},
    {"Date": "23-04-2025", "Description": "Transfer from Friend - Mike", "Deposit": 300, "Withdrawal": 0, "Balance": 6430},
    {"Date": "25-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 6250},
    {"Date": "27-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 125, "Balance": 6125},
    {"Date": "30-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5625},
    {"Date": "01-05-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7625},
    {"Date": "03-05-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 7125},
    {"Date": "05-05-2025", "Description": "Transfer from Friend - Paul", "Deposit": 200, "Withdrawal": 0, "Balance": 7325},
    {"Date": "07-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7175},
    {"Date": "10-05-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7155},
    {"Date": "12-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6905},
    {"Date": "14-05-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 250, "Withdrawal": 0, "Balance": 7155},
    {"Date": "15-05-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7025},
    {"Date": "18-05-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 7010},
    {"Date": "20-05-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 7210},
    {"Date": "22-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 6610},
    {"Date": "25-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 220, "Balance": 6390},
    {"Date": "27-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 6240},
    {"Date": "30-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5740},
    {"Date": "01-06-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7740},
    {"Date": "03-06-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7720},
    {"Date": "05-06-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 100, "Balance": 7620},
    {"Date": "07-06-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7720},
    {"Date": "10-06-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 7220},
    {"Date": "12-06-2025", "Description": "Transfer from Friend - John", "Deposit": 200, "Withdrawal": 0, "Balance": 7420},
    {"Date": "15-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 7240},
    {"Date": "17-06-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7110},
    {"Date": "18-06-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 7260},
    {"Date": "20-06-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 250, "Balance": 7010},
    {"Date": "22-06-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 7110},
    {"Date": "25-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 1000, "Balance": 6110},
    {"Date": "27-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 150, "Balance": 5960},
    {"Date": "30-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5460}
]




from datetime import date

# Add this with your other data lists
person_details = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "dob": date(1985, 7, 15).isoformat(),
        "pan": "ABCPR1234D",
        "aadhaar": "2345 6789 0123",
        "company": "Tata Consultancy Services"
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "dob": date(1990, 3, 22).isoformat(),
        "pan": "DEFPR5678E",
        "aadhaar": "3456 7890 1234",
        "company": "Infosys Technologies"
    },
    {
        "id": 3,
        "name": "Amit Kumar Singh",
        "dob": date(1982, 11, 5).isoformat(),
        "pan": "GHIPR9012F",
        "aadhaar": "4567 8901 2345",
        "company": "Wipro Limited"
    },
    {
        "id": 4,
        "name": "Neha Gupta",
        "dob": date(1995, 9, 18).isoformat(),
        "pan": "JKLMN3456G",
        "aadhaar": "5678 9012 3456",
        "company": "HDFC Bank"
    },
    {
        "id": 5,
        "name": "Vikram Joshi",
        "dob": date(1978, 2, 28).isoformat(),
        "pan": "NOPQR7890H",
        "aadhaar": "6789 0123 4567",
        "company": "Reliance Industries"
    },
    {
        "id": 6,
        "name": "Ananya Reddy",
        "dob": date(1992, 12, 8).isoformat(),
        "pan": "STUVW1234I",
        "aadhaar": "7890 1234 5678",
        "company": "ICICI Bank"
    },
    {
        "id": 7,
        "name": "Rajesh Iyer",
        "dob": date(1987, 4, 30).isoformat(),
        "pan": "XYZAB5678J",
        "aadhaar": "8901 2345 6789",
        "company": "Bharti Airtel"
    },
    {
        "id": 8,
        "name": "Deepika Menon",
        "dob": date(1993, 6, 25).isoformat(),
        "pan": "CDEFG9012K",
        "aadhaar": "9012 3456 7890",
        "company": "Larsen & Toubro"
    },
    {
        "id": 9,
        "name": "Arjun Malhotra",
        "dob": date(1980, 8, 12).isoformat(),
        "pan": "HIJKL3456L",
        "aadhaar": "0123 4567 8901",
        "company": "State Bank of India"
    },
    {
        "id": 10,
        "name": "Pooja Chatterjee",
        "dob": date(1996, 1, 7).isoformat(),
        "pan": "MNOPQ7890M",
        "aadhaar": "1234 5678 9012",
        "company": "Adani Enterprises"
    },
    {
        "id": 11,
        "name": "Sanjay Verma",
        "dob": date(1975, 5, 19).isoformat(),
        "pan": "RSTUV1234N",
        "aadhaar": "2345 6789 0123",
        "company": "Mahindra & Mahindra"
    },
    {
        "id": 12,
        "name": "Meena Deshpande",
        "dob": date(1989, 10, 3).isoformat(),
        "pan": "WXYZA5678O",
        "aadhaar": "3456 7890 1234",
        "company": "Axis Bank"
    },
    {
        "id": 13,
        "name": "Vivek Nair",
        "dob": date(1983, 7, 22).isoformat(),
        "pan": "BCDEF9012P",
        "aadhaar": "4567 8901 2345",
        "company": "Tech Mahindra"
    },
    {
        "id": 14,
        "name": "Shweta Rao",
        "dob": date(1994, 4, 14).isoformat(),
        "pan": "GHIJK3456Q",
        "aadhaar": "5678 9012 3456",
        "company": "Kotak Mahindra Bank"
    },
    {
        "id": 15,
        "name": "Rohit Khanna",
        "dob": date(1986, 9, 9).isoformat(),
        "pan": "LMNOP7890R",
        "aadhaar": "6789 0123 4567",
        "company": "Asian Paints"
    },
    {
        "id": 16,
        "name": "Anjali Mehta",
        "dob": date(1991, 2, 27).isoformat(),
        "pan": "QRSTU1234S",
        "aadhaar": "7890 1234 5678",
        "company": "Bajaj Finance"
    },
    {
        "id": 17,
        "name": "Karthik Subramanian",
        "dob": date(1979, 12, 15).isoformat(),
        "pan": "VWXYZ5678T",
        "aadhaar": "8901 2345 6789",
        "company": "Hindustan Unilever"
    },
    {
        "id": 18,
        "name": "Divya Iyer",
        "dob": date(1997, 8, 6).isoformat(),
        "pan": "ABCDE9012U",
        "aadhaar": "9012 3456 7890",
        "company": "ITC Limited"
    },
    {
        "id": 19,
        "name": "Alok Pandey",
        "dob": date(1984, 3, 11).isoformat(),
        "pan": "FGHIJ3456V",
        "aadhaar": "0123 4567 8901",
        "company": "Maruti Suzuki"
    },
    {
        "id": 20,
        "name": "Sunita Reddy",
        "dob": date(1976, 11, 23).isoformat(),
        "pan": "KLMNO7890W",
        "aadhaar": "1234 5678 9012",
        "company": "HCL Technologies"
    }
]

# Add these endpoints
@app.get("/api/person-details", summary="Get all person details")
def get_person_details():
    return person_details

@app.get("/api/person-details/{id}", summary="Get specific person by ID")
def get_person_by_id(id: int):
    person = next((p for p in person_details if p["id"] == id), None)
    return person if person else {"error": "Person not found"}

@app.get("/api/credit-details", summary="Get all credit details")
def get_credit_details():
    return credit_data



@app.get("/api/transactions", summary="Get all transaction history")
def get_transactions():
    return transactions

@app.get("/api/transactions/{index}", summary="Get specific transaction by index")
def get_transaction_by_index(index: int):
    if index < 0 or index >= len(transactions):
        return {"error": "Transaction index out of range"}
    return transactions[index]