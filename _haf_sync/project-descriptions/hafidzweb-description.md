# Student Management System (Sistem Manajemen Siswa)

## Project Overview / Gambaran Proyek

**English:**
A comprehensive web-based Student Management System built with native PHP and MySQL database. This project demonstrates fundamental web development skills including CRUD (Create, Read, Update, Delete) operations, form validation, and database management. The application allows users to manage student records with features for adding, viewing, editing, and deleting student information.

**Indonesian:**
Sistem Manajemen Siswa berbasis web yang dibangun dengan PHP native dan database MySQL. Proyek ini mendemonstrasikan keterampilan dasar pengembangan web termasuk operasi CRUD (Create, Read, Update, Delete), validasi form, dan manajemen database. Aplikasi ini memungkinkan pengguna untuk mengelola data siswa dengan fitur untuk menambah, melihat, mengedit, dan menghapus informasi siswa.

## 🔗 Live Demo
**URL:** https://hafidzweb.ct.ws

## 🛠️ Technology Stack / Stack Teknologi

- **Backend:** PHP (Native)
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Hosting:** InfinityFree
- **Server:** Apache

## 📋 Features / Fitur

### Core Functionality / Fungsi Inti:
1. **Student List (Daftar Siswa)** - View all registered students in a structured table
2. **Add Student (Tambah Siswa)** - Add new student records with form validation
3. **Edit Student (Edit Siswa)** - Modify existing student information
4. **Delete Student (Hapus Siswa)** - Remove student records from database
5. **Student Details (Detail Siswa)** - View detailed information for individual students

### Database Schema / Skema Database:
**Students Table Fields:**
- **ID** - Primary key, auto-increment
- **Name (Nama)** - Student full name (Required field)
- **NRP** - Student registration number (Required field)
- **Birth Date (Tanggal Lahir)** - Date of birth in dd/mm/yyyy format (Required field)
- **Gender (Jenis Kelamin)** - Male/Female selection with default male (Required field)
- **Description (Deskripsi)** - Additional student information (Optional field)

## 🎯 Learning Objectives / Tujuan Pembelajaran

**English:**
This project was developed as part of fundamental web development coursework at college, focusing on:
- Understanding PHP server-side programming
- Implementing CRUD operations with MySQL database
- Form handling and validation techniques
- Database design and normalization
- Web security best practices
- Deployment on shared hosting platforms

**Indonesian:**
Proyek ini dikembangkan sebagai bagian dari mata kuliah dasar pengembangan web di perguruan tinggi, dengan fokus pada:
- Memahami pemrograman server-side PHP
- Mengimplementasikan operasi CRUD dengan database MySQL
- Teknik penanganan dan validasi form
- Desain dan normalisasi database
- Praktik terbaik keamanan web
- Deployment pada platform shared hosting

## 🏗️ Project Structure / Struktur Proyek

```
hafidzweb/
├── index.php              # Homepage with navigation
├── daftarsiswa.php        # Student list with table display
├── tambahsiswa.php        # Add new student form
├── editsiswa.php          # Edit student information
├── detailsiswa.php        # View student details
├── hapussiswa.php         # Delete student record
├── config/
│   └── database.php       # Database connection configuration
├── css/
│   └── style.css          # Custom styling
└── js/
    └── script.js          # Client-side functionality
```

## 💡 Key Implementation Details / Detail Implementasi Kunci

### Form Validation:
- **Client-side:** JavaScript validation for immediate feedback
- **Server-side:** PHP validation for security and data integrity
- **Required fields:** Name, NRP, Birth Date, Gender
- **Optional fields:** Description

### Security Features:
- SQL injection prevention using prepared statements
- Input sanitization and validation
- XSS protection through proper output escaping

### User Experience:
- Intuitive navigation between pages
- Clear error messaging and validation feedback
- Responsive table design for data display
- Form pre-population for edit functionality

## 🎓 Educational Value / Nilai Edukasi

**Skills Demonstrated:**
- **Database Design:** Proper table structure and relationships
- **PHP Programming:** Server-side logic and database interactions
- **SQL Operations:** SELECT, INSERT, UPDATE, DELETE queries
- **Web Forms:** HTML form creation and PHP form processing
- **Error Handling:** Proper error management and user feedback
- **Deployment:** Live hosting setup and database configuration

## 🚀 Future Enhancements / Pengembangan Masa Depan

**Potential Improvements:**
1. **Authentication System** - User login and role management
2. **Advanced Search** - Filter and search functionality
3. **Data Export** - PDF/Excel export capabilities
4. **Image Upload** - Student photo management
5. **Pagination** - Handle large datasets efficiently
6. **API Integration** - RESTful API for external integrations
7. **Modern Framework Migration** - Upgrade to Laravel or CodeIgniter

## 📊 Project Statistics / Statistik Proyek

- **Development Time:** College semester project
- **Database Tables:** 1 main table (students)
- **CRUD Operations:** Full implementation
- **Form Fields:** 5 (4 required, 1 optional)
- **Hosting:** Free tier shared hosting (InfinityFree)

## 🔍 Code Quality / Kualitas Kode

**Best Practices Applied:**
- Separation of concerns (database, logic, presentation)
- Consistent naming conventions
- Proper commenting and documentation
- Error handling and validation
- Security considerations for web applications

---

**Note:** This project serves as a practical demonstration of fundamental web development concepts learned during college coursework. It showcases the ability to build functional web applications using core technologies without frameworks, emphasizing understanding of underlying principles.