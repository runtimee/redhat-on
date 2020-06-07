Name:           pello
Version:        0.1.1
Release:        1%{?dist}
Summary:		Say hello, in Python

License:		GPLv3+
URL:			https://example.com/%{name}
Source0:		https://example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:	python
Requires:		python
Requires:		bash
BuildArch:		noarch

%description	Compile to python byte code and run


%prep
%autosetup


%build
python -m compileall pello.py

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/


%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*


%changelog
* Sun Jun  7 2020 Cloud User
- Write python script
