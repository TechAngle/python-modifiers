# python-modifiers

<!-- Description -->
> Now, you can use access modifiers `private`, `protected` and `public` like in object-oriented languages for setting control over functions

## Install

```sh
git clone https://github.com/TechAngle/python-modifiers
cd python-modifiers
pip3 install .
```

After that you can import it via
```python
import python_modifiers
```

## About modifiers
<table>
    <thead>
        <tr>
            <th>Modifier</th>
            <th>Description</th>
            <th>Access Level</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>public</strong></td>
            <td>Accessible from any part of the program</td>
            <td>No restrictions</td>
        </tr>
        <tr>
            <td><strong>private</strong></td>
            <td>Accessible only within the class</td>
            <td>Restricted to defining scope</td>
        </tr>
        <tr>
            <td><strong>protected</strong></td>
            <td>Accessible within the class and its subclasses or related context.</td>
            <td>Limited to related scopes or subclasses</td>
        </tr>
    </tbody>
</table>

## Code example
```python
from modifiers import private, public, protected

class MyClass:
    @public
    def greet(self):
        print("Hello, this is a public method!")

    @private
    def secret(self):
        print("This is a private method!")

    @protected
    def _internal(self):
        print("This is a protected method!")

    def call_methods(self):
        self.greet()         # Should work
        self.secret()       # Should work
        self._internal()    # Should work

if __name__ == "__main__":
    obj = MyClass()
    obj.call_methods()      # Call all methods from within the class

    obj.greet()             # Should work
    try:
        obj.secret()        # Should raise an exception
    except Exception as e:
        print(e)            # Print exception message

    try:
        obj._internal()     # Should work
    except Exception as e:
        print(e)
```

## Contributing

Thank you for considering contributing to this project! Your contributions are welcome and appreciated. Here’s how you can help:

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page on GitHub to create your own copy of the repository.

2. **Clone Your Fork**: Clone your forked repository to your local machine:
```shell
git clone https://github.com/TechAngle/python-modifiers.git
```

## License

For LICENSE, go to [LICENSE](./LICENSE) file.
