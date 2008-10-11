%define module   MooseX-AttributeHelpers
%define version    0.14
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Extend your attribute interfaces
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
While the Moose manpage attributes provide you with a way to name your
accessors, readers, writers, clearers and predicates, this library provides
commonly used attribute helper methods for more specific types of data.

As seen in the the /SYNOPSIS manpage, you specify the extension via the
'metaclass' parameter. Available meta classes are:

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/MooseX

