from dga_detector import generate_random_domain, is_suspicious

def main():
    print("DGA Botnet Detection System")
    print("----------------------------")

    # generate a random domain (DGA simulation)
    domain = generate_random_domain()
    print(f"Generated Domain: {domain}")

    # check if it's suspicious
    if is_suspicious(domain):
        print("⚠️ Suspicious domain detected!")
    else:
        print("✔️ Domain seems normal.")

if __name__ == "__main__":
    main()
