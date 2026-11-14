
def show_menu():
    print("\n================================")
    print("     AI PRODUCTIVITY TOOLKIT")
    print("================================")
    print("1. Text Summarizer Prompt")
    print("2. Professional Email Generator")
    print("3. Resume Improvement Prompt")
    print("4. Coding and Debugging Assistant")
    print("5. Research Assistant")
    print("6. Exit")


def summarizer():
    text = input("Enter text to summarize: ")

    prompt = f"""
Act as a professional summarization assistant.

Summarize the following text:
{text}

Instructions:
- Identify key points.
- Use simple English.
- Remove unnecessary details.
- Present a clear summary.
"""
    return prompt


def email_generator():
    purpose = input("Email purpose: ")
    recipient = input("Recipient: ")
    details = input("Important details: ")

    prompt = f"""
Act as a professional email writing assistant.

Write an email to: {recipient}
Purpose: {purpose}
Details: {details}

Use professional language and a clear subject.
"""
    return prompt


def resume_assistant():
    role = input("Target job role: ")
    skills = input("Your skills: ")

    prompt = f"""
Act as an ATS resume assistant.

Target role: {role}
Skills: {skills}

Suggest resume improvements.
Use truthful information only.
Do not invent qualifications or experience.
"""
    return prompt


def coding_assistant():
    language = input("Programming language: ")
    problem = input("Describe the coding problem: ")

    prompt = f"""
Act as an experienced programming assistant.

Language: {language}
Problem: {problem}

Explain the solution step by step.
Provide corrected code and test cases.
Explain any errors clearly.
"""
    return prompt


def research_assistant():
    topic = input("Enter research topic: ")

    prompt = f"""
Act as a research assistant.

Research topic: {topic}

Provide:
1. Overview
2. Important findings
3. Key points
4. Reliable sources to verify
5. Conclusion

Clearly identify information that needs verification.
"""
    return prompt


def main():
    while True:
        show_menu()

        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            result = summarizer()
        elif choice == "2":
            result = email_generator()
        elif choice == "3":
            result = resume_assistant()
        elif choice == "4":
            result = coding_assistant()
        elif choice == "5":
            result = research_assistant()
        elif choice == "6":
            print("Thank you for using AI Productivity Toolkit!")
            break
        else:
            print("Invalid option. Try again.")
            continue

        print("\n========== GENERATED PROMPT ==========")
        print(result)
        print("======================================")

        save = input("Save prompt to file? (yes/no): ")

        if save.lower() == "yes":
            with open("generated_prompt.txt", "w", encoding="utf-8") as file:
                file.write(result)
            print("Prompt saved successfully!")


if __name__ == "__main__":
    main()
