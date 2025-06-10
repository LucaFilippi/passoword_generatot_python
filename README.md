# Secure Password Generator  

A Python script that generates multiple secure and customizable passwords with various complexity options.  

## Features  

- Generates one or multiple passwords in a single run  
- Customizable password length (8-64 characters)  
- Configurable character sets:  
  - Uppercase letters (A-Z)  
  - Lowercase letters (a-z)  
  - Numbers (0-9)  
  - Special symbols (!@#$%^&* etc.)  
- Input validation for all user selections  
- Simple command-line interface  

## Planned Features

- Option to save passwords to a local file

## Requirements  

- Python 3.x  
- No external dependencies required  

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/LucaFilippi/passoword_generatot_python
   cd password-generator
   ```

2. Run the script:  
   ```bash
   python password_generator.py
   ```

## Usage  

The program will guide you through:  
1. Setting password length (between 8 and 64 characters)  
2. Selecting character types to include  
3. Choosing how many passwords to generate  

## Example Session  

```
=== Secure Password Generator ===

Enter desired password length (8-64): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
How many passwords do you want? 3

Generated Passwords:
1: pK8@j7#mN2!L
2: 9x$Q5a&W3z*P
3: H6#fT2@kY9%q
```

## Implementation  

Key programming concepts demonstrated:  
- Modular function design  
- Input validation and error handling  
- Secure randomization using random.choice  
- String manipulation with the string module  
- Control flow with loops and conditionals  

## Contributing  

Contributions are welcome. Please open an issue or pull request for:  
- Bug fixes  
- New features  
- Documentation improvements  

## License  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security  

All password generation occurs locally. No passwords are stored or transmitted over networks.