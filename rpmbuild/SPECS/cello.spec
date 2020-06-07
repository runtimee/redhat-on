Name:           cello
Version:        1.0
Release:        1%{?dist}
Summary:		Hello C WORLD

License:		GPLv3+
URL:			https://example.com/#{name}
Source0:		https://example.com/#{name}/releases/%{name}-%{version}.tar.gz
Patch0:			cello-output-first-patch.patch

BuildRequires:	gcc
Requires:		make

%description
Use C to refresh a hello world program.

%prep
%autosetup

%patch0

%build
make %{?_smp_mflags}

%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Sun Jun  7 2020 Cloud User
- Program in C, again
