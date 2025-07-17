from fastapi import FastAPI
from typing import List
from datetime import date

app = FastAPI(title="Fake Credit Detail API")

# Sample credit data (20 entries)
credit_data = [
    {
        "Quarter": "Q1 2020",
        "Loan Account Status": "₹5L Personal Loan – Active",
        "Credit Card Usage/Status": "No card",
        "EMI Payment Status": "EMI Paid",
        "CIBIL Score": 710,
        "Remarks": "New loan availed"
    },
    {
        "Quarter": "Q2 2020",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "Applied",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 722,
        "Remarks": "Credit card approved"
    },
    {
        "Quarter": "Q3 2020",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "Used ₹25K / ₹100K limit",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 731,
        "Remarks": ""
    },
    {
        "Quarter": "Q4 2020",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "Used ₹35K / ₹100K",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 739,
        "Remarks": ""
    },
    {
        "Quarter": "Q1 2021",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹50K spent – paid late once",
        "EMI Payment Status": "1 Delay",
        "CIBIL Score": 727,
        "Remarks": "Slight score drop"
    },
    {
        "Quarter": "Q2 2021",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹45K used – full paid",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 734,
        "Remarks": ""
    },
    {
        "Quarter": "Q3 2021",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "Low usage",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 741,
        "Remarks": ""
    },
    {
        "Quarter": "Q4 2021",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹30K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 748,
        "Remarks": ""
    },
    {
        "Quarter": "Q1 2022",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "Consistent usage",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 755,
        "Remarks": ""
    },
    {
        "Quarter": "Q2 2022",
        "Loan Account Status": "₹5L Loan Closed",
        "Credit Card Usage/Status": "₹2L limit granted",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 765,
        "Remarks": "New loan ₹7L taken"
    },
    {
        "Quarter": "Q3 2022",
        "Loan Account Status": "₹7L Loan – Active",
        "Credit Card Usage/Status": "₹70K used / ₹2L",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 770,
        "Remarks": ""
    },
    {
        "Quarter": "Q4 2022",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹80K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 774,
        "Remarks": ""
    },
    {
        "Quarter": "Q1 2023",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹60K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 776,
        "Remarks": ""
    },
    {
        "Quarter": "Q2 2023",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹90K used – high util.",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 770,
        "Remarks": "Score dip due to utilization"
    },
    {
        "Quarter": "Q3 2023",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹40K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 775,
        "Remarks": ""
    },
    {
        "Quarter": "Q4 2023",
        "Loan Account Status": "₹7L Loan Closed",
        "Credit Card Usage/Status": "₹35K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 780,
        "Remarks": "Closed ahead of schedule"
    },
    {
        "Quarter": "Q1 2024",
        "Loan Account Status": "₹6L Loan Started",
        "Credit Card Usage/Status": "₹25K used",
        "EMI Payment Status": "On-Time (₹25,460 EMI)",
        "CIBIL Score": 782,
        "Remarks": "New EMI begins"
    },
    {
        "Quarter": "Q2 2024",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹50K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 784,
        "Remarks": ""
    },
    {
        "Quarter": "Q3 2024",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹60K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 786,
        "Remarks": ""
    },
    {
        "Quarter": "Q4 2024",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹70K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 788,
        "Remarks": ""
    },
    {
        "Quarter": "Q1 2025",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹55K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 790,
        "Remarks": ""
    },
    {
        "Quarter": "Q2 2025",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹65K used",
        "EMI Payment Status": "1 EMI bounce, paid late",
        "CIBIL Score": 779,
        "Remarks": "Auto-debit failed once"
    },
    {
        "Quarter": "Q3 2025",
        "Loan Account Status": "Active",
        "Credit Card Usage/Status": "₹50K used",
        "EMI Payment Status": "On-Time",
        "CIBIL Score": 785,
        "Remarks": "Recovered"
    }
]


# Full transaction data
transactions = [
    {"Date": "01-01-2025", "Description": "Opening Balance", "Deposit": 0, "Withdrawal": 0, "Balance": 5000},
    {"Date": "05-01-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 125000},
    {"Date": "05-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 124750},
    {"Date": "06-01-2025", "Description": "Online Purchase - Amazon Prime", "Deposit": 0, "Withdrawal": 20, "Balance": 124730},
    {"Date": "08-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 500, "Balance": 124230},
    {"Date": "10-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 124030},
    {"Date": "12-01-2025", "Description": "Transfer from Friend - John", "Deposit": 300, "Withdrawal": 0, "Balance": 124330},
    {"Date": "14-01-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 124315},
    {"Date": "15-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 124195},
    {"Date": "17-01-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 400, "Withdrawal": 0, "Balance": 124595},
    {"Date": "18-01-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 250, "Balance": 124345},
    {"Date": "20-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 124145},
    {"Date": "22-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 124015},
    {"Date": "25-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 600, "Balance": 123415},
    {"Date": "28-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 123265},
    {"Date": "30-01-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 100, "Balance": 123165},
    {"Date": "05-02-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 243165},
    {"Date": "05-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 300, "Balance": 242865},
    {"Date": "06-02-2025", "Description": "EMI Deduction", "Deposit": 0, "Withdrawal": 25460, "Balance": 217405},
    {"Date": "07-02-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 216905},
    {"Date": "10-02-2025", "Description": "Transfer from Friend - Lisa", "Deposit": 200, "Withdrawal": 0, "Balance": 217105},
    {"Date": "12-02-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 216405},
    {"Date": "13-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 216155},
    {"Date": "15-02-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 216025},
    {"Date": "18-02-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 500, "Withdrawal": 0, "Balance": 216525},
    {"Date": "20-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 216325},
    {"Date": "22-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 300, "Balance": 216025},
    {"Date": "25-02-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 216225},
    {"Date": "27-02-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 215875},
    {"Date": "05-03-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 335875},
    {"Date": "05-03-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 335855},
    {"Date": "06-03-2025", "Description": "EMI Deduction", "Deposit": 0, "Withdrawal": 25460, "Balance": 310395},
    {"Date": "07-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 310245},
    {"Date": "08-03-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 310345},
    {"Date": "10-03-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 310330},
    {"Date": "12-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 310200},
    {"Date": "14-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 309700},
    {"Date": "17-03-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 309450},
    {"Date": "18-03-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 309600},
    {"Date": "20-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 309400},
    {"Date": "22-03-2025", "Description": "Transfer from Friend - John", "Deposit": 250, "Withdrawal": 0, "Balance": 309650},
    {"Date": "25-03-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 309300},
    {"Date": "27-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 309180},
    {"Date": "30-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 308580},
    {"Date": "05-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 308430},
    {"Date": "05-04-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 428430},
    {"Date": "06-04-2025", "Description": "EMI Deduction", "Deposit": 0, "Withdrawal": 25460, "Balance": 402970},
    {"Date": "07-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 402770},
    {"Date": "10-04-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 200, "Withdrawal": 0, "Balance": 402970},
    {"Date": "12-04-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 300, "Balance": 402670},
    {"Date": "14-04-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 402770},
    {"Date": "15-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 402640},
    {"Date": "18-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 401940},
    {"Date": "20-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 250, "Balance": 401690},
    {"Date": "22-04-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 100, "Balance": 401590},
    {"Date": "23-04-2025", "Description": "Transfer from Friend - Mike", "Deposit": 300, "Withdrawal": 0, "Balance": 401890},
    {"Date": "25-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 401710},
    {"Date": "27-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 125, "Balance": 401585},
    {"Date": "30-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 401085},
    {"Date": "05-05-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 521085},
    {"Date": "05-05-2025", "Description": "Transfer from Friend - Paul", "Deposit": 200, "Withdrawal": 0, "Balance": 521285},
    {"Date": "06-05-2025", "Description": "EMI Deduction", "Deposit": 0, "Withdrawal": 25460, "Balance": 495825},
    {"Date": "07-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 495675},
    {"Date": "10-05-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 495655},
    {"Date": "12-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 495405},
    {"Date": "14-05-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 250, "Withdrawal": 0, "Balance": 495655},
    {"Date": "15-05-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 495525},
    {"Date": "18-05-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 495510},
    {"Date": "20-05-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 495710},
    {"Date": "22-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 495110},
    {"Date": "25-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 220, "Balance": 494890},
    {"Date": "27-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 494740},
    {"Date": "30-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 494240},
    {"Date": "05-06-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 100, "Balance": 494140},
    {"Date": "05-06-2025", "Description": "Salary Deposit", "Deposit": 120000, "Withdrawal": 0, "Balance": 614140},
    {"Date": "06-06-2025", "Description": "EMI Deduction", "Deposit": 0, "Withdrawal": 25460, "Balance": 588680},
    {"Date": "07-06-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 588780},
    {"Date": "10-06-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 588280},
    {"Date": "12-06-2025", "Description": "Transfer from Friend - John", "Deposit": 200, "Withdrawal": 0, "Balance": 588480},
    {"Date": "15-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 588300},
    {"Date": "17-06-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 588170},
    {"Date": "18-06-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 588320},
    {"Date": "20-06-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 250, "Balance": 588070},
    {"Date": "22-06-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 588170},
    {"Date": "25-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 1000, "Balance": 587170},
    {"Date": "27-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 150, "Balance": 587020},
    {"Date": "30-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 586520}
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