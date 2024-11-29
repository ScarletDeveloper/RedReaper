import hashlib
import itertools
import string

class Cobrelet:
    def __init__(self):
        self.char_map = {
            'a': 'af4', 'b': 'b5z', 'c': 'k9', 'd': 'd3x', 'e': 'e7y',
        }

    def transform_data(self, data):
        """Apply character map transformation to the input data."""
        return ''.join(self.char_map.get(char, char) for char in data)

    def hash(self, data, algorithm='sha256'):
        """Hash the input data using the specified algorithm."""
        transformed_data = self.transform_data(data).encode('utf-8')
        
        if algorithm == 'sha256':
            return hashlib.sha256(transformed_data).hexdigest()
        elif algorithm == 'sha1':
            return hashlib.sha1(transformed_data).hexdigest()
        elif algorithm == 'md5':
            return hashlib.md5(transformed_data).hexdigest()
        elif algorithm == 'sha512':
            return hashlib.sha512(transformed_data).hexdigest()
        else:
            raise ValueError("Unsupported hash algorithm")

    def brute_force(self, hash_value, algorithm='sha256', max_length=12):
        """Brute-force attack to find the original string that hashes to the given hash."""
        chars = string.ascii_letters + string.digits + string.punctuation
        total_attempts = 0  
        total_combinations = sum(len(chars) ** i for i in range(1, max_length + 1))

        for length in range(1, max_length + 1):
            for attempt in itertools.product(chars, repeat=length):
                attempt_string = ''.join(attempt)
                total_attempts += 1

                print(f"Attempt {total_attempts}/{total_combinations}: {attempt_string}")

                if hashlib.sha256(attempt_string.encode('utf-8')).hexdigest() == hash_value:
                    print(f"Found '{attempt_string}'!")
                    return attempt_string

        print("Failed to crack the hash.")
        return None

def main():
    red_color = "\033[31m"
    reset_color = "\033[0m"
    
    print(f"{red_color}██████╗ ███████╗██████╗     ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ ")
    print(f"{red_color}██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print(f"{red_color}██████╔╝█████╗  ██║  ██║    ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝")
    print(f"{red_color}██╔══██╗██╔══╝  ██║  ██║    ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗")
    print(f"{red_color}██║  ██║███████╗██████╔╝    ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║")
    print(f"{red_color}╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝{reset_color}")

    hash_to_crack = input("Enter the hash to crack: ")
    algorithm = input("Enter the hash algorithm (sha256, sha1, md5, sha512): ")

    cobrelet = Cobrelet()


    cobrelet.brute_force(hash_to_crack, algorithm)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
