# Secure Password Generator

A Python script that generates secure, customizable passwords with various complexity options.

## Features

- Generates passwords with combinations of:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&* etc.)
- Customizable password length
- Adjustable complexity levels
- Simple command-line interface

## Requirements

- Python 3.x
- No external dependencies required (uses built-in `random` and `string` modules)

## Usage

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Run the script:
   ```bash
   python password_generator.py
   ```

3. Follow the on-screen prompts to:
   - Set password length
   - Choose character types to include
   - Generate your password

## Example Output

```
=== Secure Password Generator ===

Enter desired password length (8-64): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Your generated password: 7x#K9@qL$2!P
```

## Implementation Details

The script demonstrates:
- Use of Python's built-in `random` module for secure randomization
- String manipulation with the `string` module
- Control flow with loops and conditionals
- Function-based modular design
- User input validation

## Contributing

Contributions are welcome! Please open an issue or pull request for any:
- Bug fixes
- New features
- Documentation improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security Note

This tool generates passwords locally on your machine. No passwords are transmitted over the network or stored anywhere.