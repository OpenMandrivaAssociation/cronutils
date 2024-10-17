Name:		cronutils
Version:	1.4
Release:	2
Summary:	Utilities to assist running batch processing jobs
Group:		System/Base 
License:	Apache 2.0
URL:		https://code.google.com/p/cronutils
Source0:	http://cronutils.googlecode.com/files/%{name}-%{version}.tar.gz


BuildRequires:	python-devel

%description
Utilities to assist running batch processing jobs.
    
    runalarm: Limit the run time of a process.
    runlock: Prevent concurrent runs of a process.
    runstat: Export statistics about a process's execution. 

%prep
%setup -q
sed -i 's/local//g' Makefile

%build
%make CC=%{__cc}

%install
%makeinstall_std

%files
%{_bindir}/runalarm
%{_bindir}/runstat
%{_bindir}/runlock
%{_mandir}/man1/*.xz
