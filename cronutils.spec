Name:		cronutils
Version:	1.1
Release:	1
Summary:	Utilities to assist running batch processing jobs
Group:		System/Base 
License:	Apache 2.0
URL:		http://code.google.com/p/cronutils
Source0:	http://cronutils.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		prefix.patch


BuildRequires:	python-devel

%description
Utilities to assist running batch processing jobs.
    
    runalarm: Limit the run time of a process.
    runlock: Prevent concurrent runs of a process.
    runstat: Export statistics about a process's execution. 

%prep
%setup -q
%patch0 -p1

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/runalarm
%{_bindir}/runstat
%{_bindir}/runlock
%{_mandir}/man1/*.xz


%changelog
* Mon Dec 12 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 740591
- imported package cronutils

