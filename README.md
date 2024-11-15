# **SDE Major Project**

## **Cloud-Based File Management System**

This project is a comprehensive cloud-based application developed using **Flask**, **AWS Cloud**, and other robust technologies. It supports file upload, download, and deletion with advanced features like **User Authentication**, **CDN Integration**, **RAID for Data Redundancy**, and **Load Balancing** across multiple EC2 instances.

---
## **System Architecture**

A simplified overview of the architecture:
![System Architecture](SDE3/Flowchart(3).png)



## **Features**

- **User Authentication:**
  - Secure login and registration system to manage user sessions.
- **File Management:**
  - Upload, download, and delete files securely.
- **CDN Integration:**
  - Faster delivery of static content using AWS CloudFront.
- **RAID Implementation:**
  - Ensures data redundancy and reliability.
- **Load Balancing:**
  - Traffic distribution across EC2 instances using AWS Elastic Load Balancer.
- **Scalable Architecture:**
  - Designed for high availability and fault tolerance.

---

## **System Architecture**



---

## **Technologies Used**

1. **Programming Language:** Python
2. **Framework:** Flask
3. **Frontend:** HTML, CSS, Jinja2 Templates
4. **Cloud Provider:** AWS (EC2, S3, CloudFront, Elastic Load Balancer)
5. **Web Server:** Nginx
6. **Backend Server:** Gunicorn
7. **Data Redundancy:** RAID (Simulated)

---

## **Installation and Setup**

Follow these steps to set up the project on your local machine or a cloud server.

### Prerequisites:
- Python 3.8+
- AWS Account
- Git
- Pip

### 1. Clone the Repository:
``` bash
git clone https://github.com/ankitkumar3440/SDE_MAjor_Project.git
cd SDE_MAjor_Project
```
---
### 2. Install Dependencies:
 ```bash
pip install -r requirements.txt
```
### 3. Run the Application:
 ```bash
python app.py
 ```
### 4. Access the Application:
 ```bash
[python app.py](http://127.0.0.1:5000
)
 ```
---
### **Deployment**
### AWS EC2 Setup:
1. Launch an EC2 instance with Amazon Linux 

2. Install necessary packages:
 ```bash
sudo yum update -y
sudo yum install python3-pip git nginx -y

 ```
3. Clone the repository and install dependencies.

---
### **Run Flask with Gunicorn:**
 ```bash
gunicorn --bind 0.0.0.0:8000 app:app

 ```
### **Configure Nginx:**
Set up Nginx as a reverse proxy for Gunicorn.

### **Load Balancer and CDN:**
1. Set up an AWS Elastic Load Balancer for multiple EC2 instances.
2. Configure AWS CloudFront for static content distribution.



