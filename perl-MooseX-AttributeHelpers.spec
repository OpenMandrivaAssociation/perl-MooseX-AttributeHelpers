%define upstream_name       MooseX-AttributeHelpers
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Extend your attribute interfaces
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version} 

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

