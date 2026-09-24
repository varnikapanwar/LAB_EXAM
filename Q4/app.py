import sys
student_count = sys.argv[1] if len(sys.argv) > 1 else "45"

report_content = f"""
COURSE ENROLMENT REPORT

Course Name      : Cloud Computing & DevOps
Students Enrolled: {student_count}

"""

with open("build_report.txt", "w") as f:
    f.write(report_content)

print(f"Successfully generated build_report.txt with {student_count} students.")
