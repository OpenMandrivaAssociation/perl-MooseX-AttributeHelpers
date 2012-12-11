%define upstream_name       MooseX-AttributeHelpers
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Extend your attribute interfaces
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
While the Moose manpage attributes provide you with a way to name your
accessors, readers, writers, clearers and predicates, this library provides
commonly used attribute helper methods for more specific types of data.

As seen in the the /SYNOPSIS manpage, you specify the extension via the
'metaclass' parameter. Available meta classes are:

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX

%changelog
* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.1
+ Revision: 485804
- update to 0.23

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 442940
- update to 0.22

* Mon Jul 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 398200
- new version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2010.0
+ Revision: 389797
- update to new version 0.20

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2010.0
+ Revision: 387012
- update to new version 0.19

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2010.0
+ Revision: 370494
- update to new version 0.17

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 292254
- update to new version 0.14

* Sat Sep 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.0
+ Revision: 281828
- import perl-MooseX-AttributeHelpers


* Sat Sep 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.0
- initial mdv release, generated with cpan2dist

