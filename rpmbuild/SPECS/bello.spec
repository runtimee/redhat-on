Name:           bello
Version:        0.1
Release:        1%{?dist}
Summary:        Hello world, in bash

License:        GPLv3+
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires:       bash
BuildArch:      noarch

%description    Time to use hello world to learn RPM with Redhat.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Sun Jun  7 2020 Cloud User
- Write bello
- Tar and copy
