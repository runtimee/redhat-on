# WIP
# SPEC to build TrustedGrub2
#
# https://github.com/runtimee/TrustedGRUB2/archive/v6.0.tar.gz
Name:		TrustedGRUB2
Version:	6.0
Release:	0
Summary:	Redhat bootloader, with TPM
License:	GPLv3+
Url:		https://github.com/runtimee/TrustedGRUB2
Source0:	https://github.com/runtimee/TrustedGRUB2/archive/v6.0.tar.gz
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64

%define _unpackaged_files_terminate_build 0
%undefine _missing_build_ids_terminate_build

# Modules code is dynamically loaded and collected from a _fixed_ path.
%define _libdir %{_exec_prefix}/lib

%ifarch %{ix86} x86_64
%define grubcpu i386
%define platform pc
%endif

%define grubarch %{grubcpu}-%{platform}
%define _bindir %{_exec_prefix}/local/bin
%define _libdir %{_exec_prefix}/local/lib
%define _etcdir %{_exec_prefix}/local/etc
%define _sbindir %{_exec_prefix}/local/sbin

%define _sharedir %{_exec_prefix}/local/share
%define _grubdir %{_sharedir}/grub
%define _infodir %{_sharedir}/info

%description
This package provides the alternatives made to transform a standard GRUB2
into a version that offers TCG (TPM) support for granting the integrity of the
boot process (trusted boot). This project was highly inspired by the former
projects TrustedGrub1 and GRUB-IMA. However TrustedGRUB2 was completely written
from scratch.

%package %{grubarch}

Summary:        Bootloader with TCG (TPM) support
Group:          System/Boot
BuildArch:      noarch

%description %{grubarch}
This package provides the alternatives made to transform a standard GRUB2
into a version that offers TCG (TPM) support for granting the integrity of the
boot process (trusted boot). This project was highly inspired by the former
projects TrustedGrub1 and GRUB-IMA. However TrustedGRUB2 was completely written
from scratch.

This package contains modules for %{platform} systems.

%prep
%autosetup -p1

mkdir build

%build
./autogen.sh
./configure
make %{?_smp_mflags}


%install
%make_install



%files
%defattr(-,root,root,-)
%{_bindir}/*

%dir %{_etcdir}/grub.d
%{_etcdir}/grub.d/*

%dir %{_etcdir}/bash_completion.d
%{_etcdir}/bash_completion.d/*

%dir %{_libdir}/grub/i386-pc
%{_libdir}/grub/i386-pc/*

%{_sbindir}/*

%dir %{_grubdir}
%{_grubdir}/grub-mkconfig_lib

%dir %{_infodir}
%{_infodir}/dir


%changelog
* Mon Mar 02 2020 Hanson Char <hchar@amazon.com> - 1.4-1
- Imported from commit 5773910: Fixed alignment erros with gcc 8
